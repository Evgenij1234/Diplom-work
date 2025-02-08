import json
import os

class CatchingMaterialsPipeline:
    def __init__(self):
        # Путь для сохранения данных в папке на уровень выше
        self.output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output.json')
        
        # Если файл существует, удаляем его, чтобы избежать накопления старых данных
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def process_item(self, item, spider):
        # Преобразуем item в формат JSON
        item_dict = {
            'name': item.get('name'),
            'link': item.get('link'),
            'price': item.get('price'),
            'unit' : item.get('unit'),
            'characteristics': item.get('characteristics')
        }

        # Сохраняем данные в файл в формате JSON
        with open(self.output_file, 'a', encoding='utf-8') as f:
            json.dump(item_dict, f, ensure_ascii=False, indent=4)
            f.write("\n")  # Каждую запись сохраняем в новой строке

        return item
