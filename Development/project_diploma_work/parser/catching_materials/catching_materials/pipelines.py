import json
import os
import atexit
import signal
import sys

class CatchingMaterialsPipeline:
    def __init__(self):
        self.output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output.json')
        self.file = None
        self.item_count = 0
        self.is_first_item = True
        self._register_signal_handlers()
        atexit.register(self._safe_close_file)

    def open_spider(self, spider):
        self.file = open(self.output_file, 'w', encoding='utf-8')
        self.file.write('[\n')
        self.file.flush()

    def _register_signal_handlers(self):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGTSTP]
        for sig in signals:
            try:
                signal.signal(sig, self._handle_signal)
            except AttributeError:
                pass

    def _handle_signal(self, signum, frame):
        sys.stderr.write(f"\nПолучен сигнал {signum}, завершаем запись JSON...\n")
        self._safe_close_file()
        sys.exit(1)

    def process_item(self, item, spider):
        try:
            item_dict = {
                'category': item.get('category', 'Не указана категория'),
                'name': item.get('name', 'Не указано название'),
                'price': item.get('price', 'Не указана цена'),
                'unit': item.get('unit', 'Не указана единица измерения'),
                'characteristics': item.get('characteristics', {'Нет характеристик': 'Нет значения'}),
                'link': item.get('link', 'Нет ссылки')
            }

            if not self.is_first_item:
                self.file.write(",\n")
            else:
                self.is_first_item = False

            self.file.write(json.dumps(item_dict, ensure_ascii=False, indent=4))
            self.file.flush() 
            self.item_count += 1

        except Exception as e:
            spider.logger.error(f"Ошибка при обработке элемента: {str(e)}")
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
            finally:
                self.file.close()
                self.file = None

    def close_spider(self, spider):
        self._safe_close_file()