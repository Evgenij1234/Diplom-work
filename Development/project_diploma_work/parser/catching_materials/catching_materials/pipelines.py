import json
import os

class CatchingMaterialsPipeline:
    def __init__(self):
        self.output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output.json')
        self.file = open(self.output_file, 'w', encoding='utf-8')
        self.file.write('[') 

    def process_item(self, item, spider):
        item_dict = {}

        def clean_description(text):
            if text:
                text = ' '.join(text.split()) 
            return text.strip() if text else text

        if item.get('category'):
            item_dict['category'] = item['category']
        if item.get('name'):
            item_dict['name'] = item['name']
        if item.get('price'):
            item_dict['price'] = item['price']

        item_dict['unit'] = item.get('unit', 'Не указана единица измерения')
        item_dict['characteristics'] = clean_description(item.get('characteristics', 'Нет описания'))
        item_dict['link'] = item.get('link', 'Нет ссылки')

        self.file.write(json.dumps(item_dict, ensure_ascii=False, indent=4))
        self.file.write(",\n") 

        return item

    def close_spider(self, spider):
        self.file.write(']\n')
        self.file.close()
