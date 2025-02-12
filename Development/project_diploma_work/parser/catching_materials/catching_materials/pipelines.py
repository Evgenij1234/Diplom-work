import json
import os

class CatchingMaterialsPipeline:
    def __init__(self):
        # Путь для сохранения данных в папке на уровень выше
        self.output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output.json')
        
        # Открываем файл для записи один раз в начале работы паука
        self.file = open(self.output_file, 'w', encoding='utf-8')
        self.file.write('[')  # Начинаем JSON-массив

    def process_item(self, item, spider):
        # Собираем данные для записи, проверяя обязательные поля
        item_dict = {}

        # Функция для очистки описания от лишних пробелов
        def clean_description(text):
            if text:
                text = ' '.join(text.split())  # Заменяем несколько пробелов на один
            return text.strip() if text else text

        # Проверка обязательных полей на наличие данных, а не пустых строк
        if item.get('category'):
            item_dict['category'] = item['category']
        if item.get('name'):
            item_dict['name'] = item['name']
        if item.get('price'):
            item_dict['price'] = item['price']
        
        # Прочие поля записываем всегда, даже если они пустые
        item_dict['link'] = item.get('link', 'Нет ссылки')
        item_dict['unit'] = item.get('unit', 'Не указана единица измерения')
        
        # Для описания товара удаляем лишние пробелы
        item_dict['characteristics'] = clean_description(item.get('characteristics', 'Нет описания'))

        # Записываем данные в файл. После каждого товара добавляем запятую, если это не последний товар.
        self.file.write(json.dumps(item_dict, ensure_ascii=False, indent=4))

        # Если это не последний элемент, ставим запятую для продолжения массива
        self.file.write(",\n") 

        return item

    def close_spider(self, spider):
        # Закрываем JSON-массив и файл после завершения работы паука
        self.file.write(']\n')
        self.file.close()
