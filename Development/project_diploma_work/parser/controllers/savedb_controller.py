from flask import Blueprint, jsonify
import json
import os
from models.product import Product
from extensions import db
import logging
from dateutil import parser  # используем dateutil для гибкого разбора даты

savedb_bp = Blueprint('savedb', __name__)

# Настройка логгера
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

DATA_FOLDER = os.path.join('catching_materials', 'catching_materials', 'data')

@savedb_bp.route('/savedb/<username>', methods=['POST'])

def save_to_db(username):
    try:
        logger.info(f"Начинаем процесс сохранения для пользователя: {username}")
        
        filename = f"{username}_data.json"
        filepath = os.path.join(DATA_FOLDER, filename)
        logger.info(f"Ищем файл: {filepath}")
        
        if not os.path.exists(filepath):
            logger.error(f"Файл не найден: {filepath}")
            return jsonify({'error': 'Файл с данными не найден'}), 404
        
        with open(filepath, 'r', encoding='utf-8') as f:
            products_data = json.load(f)
        
        if not isinstance(products_data, list):
            logger.error("Неверный формат данных: ожидается список")
            return jsonify({'error': 'Неверный формат данных'}), 400
        
        saved_count = 0
        errors = []
        
        for i, product_data in enumerate(products_data):
            try:
                # Автоматический разбор даты
                date_time = parser.parse(product_data['date_time']) if 'date_time' in product_data else None
                
                product = Product(
                    user=username,
                    category=product_data.get('category'),
                    name=product_data['name'],  # обязательное поле
                    price=float(product_data['price'].replace(' ', '')) if 'price' in product_data else None,
                    unit=product_data.get('unit'),
                    characteristics=product_data.get('characteristics'),
                    link=product_data.get('link'),
                    resource=product_data.get('resource'),
                    date_time=date_time
                )
                
                db.session.add(product)
                saved_count += 1
                logger.debug(f"Добавлен товар {i}: {product_data.get('name')}")
                
            except Exception as e:
                error_msg = f"Ошибка с товаром {i}: {str(e)}"
                logger.error(error_msg, exc_info=True)
                errors.append(error_msg)
                continue
        
        db.session.commit()
        logger.info(f"Успешно сохранено: {saved_count} из {len(products_data)} товаров")
        
        response = {
            'message': 'Данные сохранены',
            'saved': saved_count,
            'total': len(products_data),
            'errors': errors if errors else None
        }
        
        # Декодируем UTF-8 в ответе перед отправкой
        response = json.dumps(response, ensure_ascii=False)
        
        return response, 200
        
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка чтения JSON: {str(e)}")
        return jsonify({'error': 'Ошибка чтения JSON'}), 400
    except Exception as e:
        db.session.rollback()
        logger.error(f"Критическая ошибка: {str(e)}", exc_info=True)
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500


