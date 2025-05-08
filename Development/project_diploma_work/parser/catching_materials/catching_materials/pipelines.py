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
        self.data_dir = os.path.join(base_dir, '.', 'data')
        
        # Создаем папку если ее нет
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Инициализация переменных
        self.file = None
        self.item_count = 0
        self.is_first_item = True
        self.current_user = None
        self.output_file_path = None
        
        # Обязательные поля, которые должны быть в item
        self.required_fields = ['user', 'category', 'name', 'price', 'link']
        
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

    def open_spider(self, spider):
        self.temp_logger.info("Ожидаем первого элемента для определения пользователя")

    def _validate_item(self, item):
        """Проверка наличия обязательных полей и обработка цены"""
        # Проверяем обязательные поля
        missing_fields = [field for field in self.required_fields if field not in item or not item[field]]
        if missing_fields:
            raise ValueError(f"Отсутствуют обязательные поля: {', '.join(missing_fields)}")

        # Обрабатываем цену
        if 'price' in item:
            price = str(item['price']).strip()
            if price:  # Если цена не пустая
                # Обрезаем всё после точки или запятой
                price = price.split('.')[0].split(',')[0]
                # Удаляем все нецифровые символы (кроме минуса для отрицательных чисел)
                price = ''.join(c for c in price if c.isdigit() or c == '-')
                # Если после обработки получили пустую строку - ставим 0
                item['price'] = price if price else '0'
            else:
                item['price'] = '0'

        return item

    def process_item(self, item, spider):
        try:
            # Валидация и обработка полей
            item = self._validate_item(item)
            
            user = item.get('user', 'unknown_user')
            
            # Если это первый элемент, инициализируем файлы для пользователя
            if self.current_user is None:
                self.current_user = user
                safe_user = "".join(c if c.isalnum() else "_" for c in user)
                self.output_file_path = os.path.join(self.data_dir, f"{safe_user}_data.json")
                
                try:
                    self.file = open(self.output_file_path, 'w', encoding='utf-8')
                    self.file.write('[\n')
                    self.file.flush()
                    self.temp_logger.info(f"Открыт файл для записи результатов: {self.output_file_path}")
                except Exception as e:
                    self.temp_logger.error(f"Ошибка при открытии файла {self.output_file_path}: {str(e)}", exc_info=True)
                    raise

            item_dict = {
                'user': user,
                'category': item.get('category', 'Не указана категория'),
                'name': item.get('name', 'Не указано название'),
                'price': item.get('price', '0'),  # После обработки всегда будет значение
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
            
        except ValueError as e:
            self.temp_logger.error(f"Элемент не сохранен: {str(e)}")
            raise
        except Exception as e:
            self.temp_logger.error(f"Ошибка при обработке элемента: {str(e)}", exc_info=True)
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
                else:
                    self.temp_logger.info(f"Файл {self.output_file_path} закрыт. Всего элементов: {self.item_count}")
            except Exception as e:
                if hasattr(self, 'logger'):
                    self.logger.error(f"Ошибка при закрытии файла: {str(e)}", exc_info=True)
                else:
                    self.temp_logger.error(f"Ошибка при закрытии файла: {str(e)}", exc_info=True)
            finally:
                self.file.close()
                self.file = None

    def close_spider(self, spider):
        self.temp_logger.info("Завершение работы паука")
        self._safe_close_file()