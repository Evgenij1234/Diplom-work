from flask import Flask
from flask_cors import CORS
from controllers.scrapy_controller import scrapy_bp
from controllers.log_data_controller import log_data_bp

app = Flask(__name__)
CORS(app)

# Регистрация Blueprints
app.register_blueprint(scrapy_bp)
app.register_blueprint(log_data_bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)