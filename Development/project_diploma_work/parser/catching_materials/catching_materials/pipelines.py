import json
import os
import atexit
import signal
import sys
import logging
from scrapy.utils.log import configure_logging

class CatchingMaterialsPipeline:
    def __init__(self):
        # Определяем базовую директорию
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(base_dir, '..', 'data')
        self.logs_dir = os.path.join(base_dir, '..', 'logs')
        
        # Создаем папки если их нет
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Инициализация переменных
        self.file = None
        self.item_count = 0
        self.is_first_item = True
        self.current_user = None
        self.output_file_path = None
        self.log_file_path = None
        
        # Настройка временного логгера до получения информации о пользователе
        self._setup_temp_logging()
        self.temp_logger = logging.getLogger('TempCatchingMaterialsPipeline')
        
        # Регистрация обработчиков сигналов
        self._register_signal_handlers()
        atexit.register(self._safe_close_file)

    def _setup_temp_logging(self):
        """Временная настройка логирования до получения информации о пользователе"""
        configure_logging(install_root_handler=False)
        
        # Настройка временного вывода только в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)

    def _setup_user_logging(self, user):
        """Настройка системы логирования для конкретного пользователя"""
        # Очищаем предыдущие обработчики
        root_logger = logging.getLogger()
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        
        # Создаем форматтер
        formatter = logging.Formatter(
            '%(asctime)s [%(name)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Обработчик для записи в файл
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        
        # Обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        
        # Настраиваем корневой логгер
        root_logger.setLevel(logging.INFO)
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)
        
        # Логгер для этого пайплайна
        self.logger = logging.getLogger(f'CatchingMaterialsPipeline_{user}')
        self.logger.info(f"Инициализирован логгер для пользователя {user}. Логи будут записываться в {self.log_file_path}")

    def open_spider(self, spider):
        # Пока не знаем пользователя, используем временный логгер
        self.temp_logger.info("Ожидаем первого элемента для определения пользователя")

    def _register_signal_handlers(self):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGTSTP]
        for sig in signals:
            try:
                signal.signal(sig, self._handle_signal)
            except Exception as e:
                logger = self.logger if hasattr(self, 'logger') else self.temp_logger
                logger.warning(f"Не удалось зарегистрировать обработчик сигнала {sig}: {str(e)}")

    def _handle_signal(self, signum, frame):
        logger = self.logger if hasattr(self, 'logger') else self.temp_logger
        logger.warning(f"Получен сигнал {signum}, завершаем работу...")
        self._safe_close_file()
        if signum == signal.SIGTSTP:
            signal.signal(signum, signal.SIG_DFL)
            os.kill(os.getpid(), signum)
        else:
            sys.exit(1)

    def process_item(self, item, spider):
        try:
            user = item.get('user', 'unknown_user')
            
            # Если это первый элемент, инициализируем файлы для пользователя
            if self.current_user is None:
                self.current_user = user
                # Создаем безопасное имя файла
                safe_user = "".join(c if c.isalnum() else "_" for c in user)
                self.output_file_path = os.path.join(self.data_dir, f"{safe_user}_data.json")
                self.log_file_path = os.path.join(self.logs_dir, f"{safe_user}_pipeline.log")
                
                # Настраиваем логирование для пользователя
                self._setup_user_logging(user)
                
                # Открываем файл для записи данных
                try:
                    self.file = open(self.output_file_path, 'w', encoding='utf-8')
                    self.file.write('[\n')
                    self.file.flush()
                    self.logger.info(f"Открыт файл для записи результатов: {self.output_file_path}")
                except Exception as e:
                    self.logger.error(f"Ошибка при открытии файла {self.output_file_path}: {str(e)}", exc_info=True)
                    raise

            item_dict = {
                'user': user,
                'category': item.get('category', 'Не указана категория'),
                'name': item.get('name', 'Не указано название'),
                'price': item.get('price', 'Не указана цена'),
                'unit': item.get('unit', 'Не указана единица измерения'),
                'characteristics': item.get('characteristics', {'Нет характеристик': 'Нет значения'}),
                'link': item.get('link', 'Нет ссылки'),
                'resource': item.get('resource', 'Ресурс не получен'),
                'date_time': item.get('date_time', 'Дата и время не получены')
            }

            if not self.is_first_item:
                self.file.write(",\n")
            else:
                self.is_first_item = False

            json_line = json.dumps(item_dict, ensure_ascii=False, indent=4)
            self.file.write(json_line)
            self.file.flush()
            self.item_count += 1
            
            # Логируем каждые 10 элементов для примера
            if self.item_count % 10 == 0:
                self.logger.debug(f"Обработан элемент {self.item_count}: {item.get('name', 'Без названия')[:50]}...")
                
        except Exception as e:
            self.logger.error(f"Ошибка при обработке элемента: {str(e)}", exc_info=True)
            raise

        return item

    def _safe_close_file(self):
        if getattr(self, 'file', None) and not self.file.closed:
            try:
                if self.item_count > 0:
                    self.file.write('\n]\n')
                else:
                    self.file.write(']\n')
                self.file.flush()
                if hasattr(self, 'logger'):
                    self.logger.info(f"Файл {self.output_file_path} закрыт. Всего элементов: {self.item_count}")
            except Exception as e:
                if hasattr(self, 'logger'):
                    self.logger.error(f"Ошибка при закрытии файла: {str(e)}", exc_info=True)
            finally:
                self.file.close()
                self.file = None

    def close_spider(self, spider):
        if hasattr(self, 'logger'):
            self.logger.info("Завершение работы паука")
        self._safe_close_file()