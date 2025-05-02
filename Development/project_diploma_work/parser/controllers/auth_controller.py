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
            return jsonify({'error': 'No data provided'}), 400
            
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
            
        if len(username) < 4:
            return jsonify({'error': 'Username must be at least 4 characters'}), 400
            
        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400
            
        # Проверка существования пользователя
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 409
            
        # Создание нового пользователя
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        # Генерация токена
        access_token = create_access_token(
            identity=new_user.id,
            expires_delta=timedelta(days=7)
        )
        
        logger.info(f"New user registered: {username}")
        
        return jsonify({
            'message': 'User registered successfully',
            'access_token': access_token,
            'user_id': new_user.id,
            'username': new_user.username
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Registration error: {str(e)}")
        return jsonify({'error': 'Registration failed'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Валидация входных данных
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
            
        # Поиск пользователя
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401
            
        # Генерация токена
        access_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(days=7))
        
        logger.info(f"User logged in: {username}")
        
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user_id': user.id,
            'username': user.username
        }), 200
        
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({'error': 'Login failed'}), 500

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
            
        return jsonify({
            'message': 'Protected endpoint accessed successfully',
            'user_id': user.id,
            'username': user.username
        }), 200
        
    except Exception as e:
        logger.error(f"Protected endpoint error: {str(e)}")
        return jsonify({'error': 'Access denied'}), 403

@auth_bp.route('/validate-token', methods=['GET'])
@jwt_required()
def validate_token():
    """Эндпоинт для проверки валидности токена"""
    current_user_id = get_jwt_identity()
    return jsonify({'valid': True, 'user_id': current_user_id}), 200