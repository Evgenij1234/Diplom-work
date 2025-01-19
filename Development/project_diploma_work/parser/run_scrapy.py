from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_scrapy', methods=['GET'])
def run_scrapy():
    # Запуск Scrapy спайдера
    result = subprocess.run(['scrapy', 'crawl', 'your_spider_name'], capture_output=True, text=True)
    
    # Проверка результата выполнения
    if result.returncode == 0:
        return jsonify({'status': 'success', 'output': result.stdout})
    else:
        return jsonify({'status': 'error', 'output': result.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
