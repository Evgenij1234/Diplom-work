from flask import Flask, jsonify, request
from flask_cors import CORS  # <--- добавлено
import subprocess
import shlex
import os
import signal
import atexit
import time

app = Flask(__name__)
CORS(app)

scrapy_processes = {}  # Словарь для хранения процессов Scrapy для разных пользователей

@app.route('/')
def hello():
    return "Hello, this is your Scrapy Flask serveraaa!"

@app.route('/start-scrapy', methods=['POST'])
def start_scrapy():
    user_id = request.json.get("user_id")  # Уникальный идентификатор пользователя

    # Проверка, не запущен ли уже процесс для этого пользователя
    if user_id in scrapy_processes and scrapy_processes[user_id].poll() is None:
        return jsonify({"status": f"Scrapy spider is already running for user {user_id}."}), 400

    data = request.json

    args = {
        "user": user_id, 
        "start_url": data.get("start_url"),
        "allowed_domains": data.get("allowed_domains"),
        "product_path": data.get("product_path"),
        "category_selector": data.get("category_selector"),
        "name_selector": data.get("name_selector"),
        "price_selector": data.get("price_selector"),
        "unit_selector": data.get("unit_selector"),
        "block_selector": data.get("block_selector"),
        "key_selector": data.get("key_selector"),
        "value_selector": data.get("value_selector"),
    }

    # Команда
    cmd = "cd catching_materials && scrapy crawl spider_main"
    for key, value in args.items():
        if value is not None:
            cmd += f" -a {key}={shlex.quote(value)}"

    print(f"Запускаем Scrapy для пользователя {user_id}:")
    print(cmd)

    try:
        # Запускаем Scrapy как фоновый процесс для этого пользователя
        scrapy_process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, preexec_fn=os.setsid
        )

        # Сохраняем процесс в словаре по ключу user_id
        scrapy_processes[user_id] = scrapy_process

        # Регистрация обработчика для корректного завершения
        atexit.register(handle_exit, user_id)
        return jsonify({"status": f"Scrapy spider started for user {user_id}."}), 200

    except Exception as e:
        return jsonify({
            "status": "Error in starting Scrapy spider.",
            "error": str(e)
        }), 500


def handle_exit(user_id):
    if user_id in scrapy_processes:
        scrapy_process = scrapy_processes[user_id]
        if scrapy_process.poll() is None:
            print(f" Процесс для пользователя {user_id} завершён, завершаем работу Scrapy")
            os.killpg(os.getpgid(scrapy_process.pid), signal.SIGTERM)
        del scrapy_processes[user_id]  # Удаляем процесс из словаря

@app.route('/stop-scrapy', methods=['POST'])
def stop_scrapy():
    user_id = request.json.get("user_id")

    if user_id not in scrapy_processes or scrapy_processes[user_id].poll() is not None:
        return jsonify({"status": f"No running Scrapy process for user {user_id}."}), 400

    try:
        os.killpg(os.getpgid(scrapy_processes[user_id].pid), signal.SIGTERM)
        del scrapy_processes[user_id]  # Удаляем процесс из словаря
        return jsonify({"status": f"Scrapy spider stopped for user {user_id}."}), 200
    except Exception as e:
        return jsonify({
            "status": "Error stopping Scrapy spider.",
            "error": str(e)
        }), 500

# 🔽 Новый маршрут: Получение логов
@app.route('/get-log', methods=['GET'])
def get_log():
    user_id = request.args.get("user_id")
    log_file_path = f"./catching_materials/logs/{user_id}_pipeline.log"

    timeout = 30  # секунд
    interval = 1  # проверка каждую секунду
    waited = 0

    while not os.path.exists(log_file_path) and waited < timeout:
        time.sleep(interval)
        waited += interval

    if not os.path.exists(log_file_path):
        return jsonify({"status": "Log file not found after waiting.", "user_id": user_id}), 404

    with open(log_file_path, 'r', encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return jsonify({"status": "success", "log": content})

# 🔽 Новый маршрут: Получение данных
@app.route('/get-data', methods=['GET'])
def get_data():
    user_id = request.args.get("user_id")
    data_file_path = f"./catching_materials/data/{user_id}_data.json"

    timeout = 30
    interval = 1
    waited = 0

    while not os.path.exists(data_file_path) and waited < timeout:
        time.sleep(interval)
        waited += interval

    if not os.path.exists(data_file_path):
        return jsonify({"status": "Data file not found after waiting.", "user_id": user_id}), 404

    with open(data_file_path, 'r', encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return jsonify({"status": "success", "data": content})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
