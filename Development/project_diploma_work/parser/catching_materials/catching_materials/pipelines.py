import json
from itemadapter import ItemAdapter


class CatchingMaterialsPipeline:
    def process_item(self, item, spider):
        print(item)
        return item


class JsonWriterPipeline:
    def open_spider(self, spider):
        # Открываем файл для записи при запуске паука
        self.file = open('output.json', 'w', encoding='utf-8')
        self.file.write('[')  # Начало JSON-массива

    def close_spider(self, spider):
        # Закрываем файл при завершении паука
        self.file.write(']')  # Конец JSON-массива
        self.file.close()

    def process_item(self, item, spider):
        # Сохраняем каждый элемент (item) в файл
        line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(line)
        return item