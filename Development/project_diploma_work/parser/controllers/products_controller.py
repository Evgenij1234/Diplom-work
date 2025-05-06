from flask import Blueprint, request, jsonify, Response
from models.product import Product
from extensions import db
from datetime import datetime
import json
import logging

products_bp = Blueprint('products', __name__)
logger = logging.getLogger(__name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    try:
        # Получаем параметры запроса
        user = request.args.get('user')
        resource = request.args.get('resource')
        category = request.args.get('category')
        name = request.args.get('name')
        time_start = request.args.get('time_start')
        time_end = request.args.get('time_end')

        # Проверяем обязательный параметр user
        if not user:
            return jsonify({'error': 'Параметр "user" обязателен'}), 400

        # Начинаем формировать запрос
        query = Product.query.filter_by(user=user)

        # Добавляем фильтры, если параметры переданы
        if resource:
            query = query.filter(Product.resource == resource)
        if category:
            query = query.filter(Product.category == category)
        if name:
            query = query.filter(Product.name.ilike(f'%{name}%'))

        # Фильтрация по дате
        if time_start or time_end:
            try:
                if time_start:
                    start_date = datetime.strptime(time_start, '%Y-%m-%dT%H:%M:%S')
                    query = query.filter(Product.date_time >= start_date)
                if time_end:
                    end_date = datetime.strptime(time_end, '%Y-%m-%dT%H:%M:%S')
                    query = query.filter(Product.date_time <= end_date)
            except ValueError as e:
                return jsonify({'error': f'Неверный формат даты. Используйте YYYY-MM-DDTHH:MM:SS. Ошибка: {str(e)}'}), 400

        # Выполняем запрос
        products = query.order_by(Product.date_time.desc()).all()

        # Формируем ответ с поддержкой кириллицы
        result = {
            'count': len(products),
            'products': [{
                'id': product.id,
                'user': product.user,
                'category': product.category,
                'name': product.name,
                'price': float(product.price) if product.price else None,
                'unit': product.unit,
                'characteristics': product.characteristics,
                'link': product.link,
                'resource': product.resource,
                'date_time': product.date_time.isoformat() if product.date_time else None,
                'created_at': product.created_at.isoformat() if product.created_at else None
            } for product in products]
        }

        # Возвращаем ответ с отключенным ensure_ascii
        return Response(
            json.dumps(result, ensure_ascii=False),
            mimetype='application/json; charset=utf-8'
        ), 200

    except Exception as e:
        logger.error(f"Ошибка при получении продуктов: {str(e)}", exc_info=True)
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500