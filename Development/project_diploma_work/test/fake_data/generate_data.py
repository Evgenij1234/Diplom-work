import json
import sys
import os
import random
from argparse import ArgumentParser

def update_json_data(json_file, new_datetime=None):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated_prices = 0
        
        for item in data:
            # Обновляем дату у всех, если указана
            if new_datetime:
                item['date_time'] = new_datetime
            
            # Обновляем цену у всех товаров с рандомным отклонением от +0% до +5%
            if 'price' in item and item['price']:
                try:
                    current_price = float(item['price'])
                    # Вычисляем 5% от текущей цены
                    five_percent = current_price * 0.05
                    # Генерируем случайное отклонение от 0 до 5%
                    random_deviation = random.uniform(0, five_percent)
                    # Новая цена с отклонением
                    new_price = round(current_price + random_deviation, 2)
                    item['price'] = str(new_price)
                    updated_prices += 1
                except (ValueError, TypeError):
                    continue
        
        if new_datetime:
            print(f"✓ Обновлено date_time для {len(data)} объектов")
        print(f"✓ Обновлено цен для {updated_prices} объектов (+0% до +5% от исходной)")
        
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
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"Ошибка: Файл {args.file} не найден!")
        sys.exit(1)
    
    if args.datetime is None:
        print("✓ Будут обновлены только цены (+0% до +5% от текущих)")
    
    update_json_data(args.file, args.datetime)

if __name__ == "__main__":
    main()
