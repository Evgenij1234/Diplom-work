import os
from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from extensions import db
from controllers.scrapy_controller import scrapy_bp
from controllers.auth_controller import auth_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    # Конфигурация JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'fallback-secret-key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    
    # Конфигурация CORS
    CORS(app)
    
    # Конфигурация базы данных
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Инициализация расширений
    jwt = JWTManager(app)
    db.init_app(app)
    
    # Регистрация Blueprints
    app.register_blueprint(scrapy_bp)
    app.register_blueprint(auth_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'True') == 'True', 
            host=os.getenv('FLASK_HOST', '0.0.0.0'), 
            port=int(os.getenv('FLASK_PORT', '5000')))