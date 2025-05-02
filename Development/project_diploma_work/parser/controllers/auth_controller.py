from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import check_password_hash
from models.user import User
from extensions import db
from datetime import timedelta
import logging

auth_bp = Blueprint('auth', __name__)
logger = logging.getLogger(__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Валидация входных данных
        if not data:
            return jsonify({'error': 'Не предоставлены данные'}), 400
            
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Требуется имя пользователя и пароль'}), 400
            
        if len(username) < 4:
            return jsonify({'error': 'Имя пользователя должно быть не менее 4 символов'}), 400
            
        if len(password) < 6:
            return jsonify({'error': 'Пароль должен быть не менее 6 символов'}), 400
            
        # Проверка существования пользователя
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Пользователь с таким именем уже существует'}), 409
            
        # Создание нового пользователя
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        # Генерация токена с явным преобразованием ID в строку
        access_token = create_access_token(
            identity=str(new_user.id),  # Важное исправление здесь!
            expires_delta=timedelta(days=7)
        )
        
        logger.info(f"Новый пользователь зарегистрирован: {username}")
        
        return jsonify({
            'message': 'Пользователь успешно зарегистрирован',
            'access_token': access_token,
            'user_id': new_user.id,
            'username': new_user.username
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Ошибка регистрации: {str(e)}", exc_info=True)
        return jsonify({'error': 'Ошибка регистрации'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Не предоставлены данные'}), 400
            
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Требуется имя пользователя и пароль'}), 400
            
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            return jsonify({'error': 'Неверное имя пользователя или пароль'}), 401
            
        # Явное преобразование ID в строку
        access_token = create_access_token(
            identity=str(user.id),  # Важное исправление здесь!
            expires_delta=timedelta(days=7)
        )
        
        logger.info(f"Пользователь вошел в систему: {username}")
        
        return jsonify({
            'message': 'Вход выполнен успешно',
            'access_token': access_token,
            'user_id': user.id,
            'username': user.username
        }), 200
        
    except Exception as e:
        logger.error(f"Ошибка входа: {str(e)}", exc_info=True)
        return jsonify({'error': 'Ошибка входа'}), 500

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({'error': 'Пользователь не найден'}), 404
            
        return jsonify({
            'message': 'Доступ к защищенному ресурсу получен',
            'user_id': user.id,
            'username': user.username
        }), 200
        
    except Exception as e:
        logger.error(f"Ошибка защищенного эндпоинта: {str(e)}", exc_info=True)
        return jsonify({'error': 'Доступ запрещен'}), 403

@auth_bp.route('/validate-token', methods=['GET'])
@jwt_required()
def validate_token():
    try:
        current_user_id = get_jwt_identity()
        if not current_user_id:
            return jsonify({'valid': False, 'error': 'Неверный токен'}), 401
            
        return jsonify({
            'valid': True,
            'user_id': current_user_id
        }), 200
    except Exception as e:
        logger.error(f"Ошибка валидации токена: {str(e)}", exc_info=True)
        return jsonify({'valid': False, 'error': 'Ошибка валидации токена'}), 400