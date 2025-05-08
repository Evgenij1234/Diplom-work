import json
import sys
import os
from argparse import ArgumentParser

def update_json_data(json_file, new_datetime=None, search_name=None, new_price=None):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated_items = 0
        
        for item in data:
            # Обновляем дату у всех, если указана
            if new_datetime:
                item['date_time'] = new_datetime
                updated_items += 1
            
            # Обновляем цену только у подходящих по name
            if search_name and new_price is not None and item.get('name') == search_name:
                item['price'] = str(new_price)
                print(f"✓ Обновлена цена для '{search_name}': {new_price}₽")
        
        if new_datetime:
            print(f"✓ Обновлено date_time для {len(data)} объектов")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        return True
    
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        return False

def main():
    parser = ArgumentParser(description='Обновление JSON файла')
    parser.add_argument('file', help='Путь к JSON файлу')
    parser.add_argument('--datetime', help='Новая дата (YYYY-MM-DD HH:MM:SS)', default=None)
    parser.add_argument('--name', help='Имя товара для обновления цены', default=None)
    parser.add_argument('--price', help='Новая цена (требует --name)', type=float, default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"Ошибка: Файл {args.file} не найден!")
        sys.exit(1)
    
    if args.price is not None and args.name is None:
        print("Ошибка: --price требует --name")
        sys.exit(1)
    
    if args.datetime is None and args.name is None:
        print("Ошибка: Не указано что обновлять (--datetime и/или --name + --price)")
        sys.exit(1)
    
    update_json_data(args.file, args.datetime, args.name, args.price)

if __name__ == "__main__":
    main()