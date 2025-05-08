# Только обновить дату у всех:
python3 script.py data.json --datetime "2025-05-10 00:00:00"
пример:
python3 generate_data.py user123_data.json --datetime "2025-05-10 12:00:00" 

# Только обновить цену у конкретного товара:
python3 script.py data.json --name "имя" --price 2000
пример:
python3 generate_data.py user123_data.json --name "Фиброцементный сайдинг красный ГОСТ 18124-2012" --price 5000

# Обновить и дату, и цену:
python3 script.py data.json --datetime "2025-05-10 00:00:00" --name "Шпатлевка гипсовая Seneco PL54, 20 кг" --price 400
пример:
python3 generate_data.py user123_data.json --datetime "2025-05-23 00:00:00" --name "Шпатлевка гипсовая Seneco PL54, 20 кг" --price 400