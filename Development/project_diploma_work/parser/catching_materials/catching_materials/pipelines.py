import json
import os

class CatchingMaterialsPipeline:
    def __init__(self):
        self.output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output.json')
        self.file = open(self.output_file, 'w', encoding='utf-8')
        self.file.write('[') 
        self.item_count = 0

    def process_item(self, item, spider):
        item_dict = {}

        item_dict['category'] = item.get('category', 'Не указана категория')
        item_dict['name'] = item.get('name', 'Не указано название')
        item_dict['price'] = item.get('price', 'Не указана цена')
        item_dict['unit'] = item.get('unit', 'Не указана единица измерения')
        
        # Характеристики
        item_dict['characteristics'] = item.get('characteristics', {'Нет характеристик': 'Нез значения'})

        item_dict['link'] = item.get('link', 'Нет ссылки')
        self.item_count += 1
        if self.item_count > 1:
            self.file.write(",\n")
        self.file.write(json.dumps(item_dict, ensure_ascii=False, indent=4))
        return item

    def close_spider(self, spider):
        self.file.write('\n]\n')
        self.file.close()