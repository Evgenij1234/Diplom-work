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

        def clean_description(text):
            if text:
                text = ' '.join(text.split()) 
            return text.strip() if text else text
        item_dict['category'] = item['category']
        item_dict['name'] = item['name']
        item_dict['price'] = item['price']
        item_dict['unit'] = item.get('unit', 'Не указана единица измерения')
        item_dict['characteristics'] = clean_description(item.get('characteristics', 'Нет описания'))
        item_dict['link'] = item.get('link', 'Нет ссылки')
        self.item_count += 1
        if self.item_count > 1:
            self.file.write(",\n")
        self.file.write(json.dumps(item_dict, ensure_ascii=False, indent=4))
        return item

    def close_spider(self, spider):
        self.file.write('\n]\n')
        self.file.close()
