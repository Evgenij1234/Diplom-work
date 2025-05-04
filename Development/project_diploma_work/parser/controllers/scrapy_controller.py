from flask import Blueprint, jsonify, request, send_file
import subprocess
import shlex
import os
import signal
import atexit
from io import StringIO
import tempfile
import time

scrapy_bp = Blueprint('scrapy', __name__)
scrapy_processes = {}
scrapy_logs = {}  # Для хранения логов в памяти

@scrapy_bp.route('/')
def hello():
    return "Hello!"

@scrapy_bp.route('/start-scrapy', methods=['POST'])
def start_scrapy():
    user_id = request.json.get("user_id")
    
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

    cmd = "cd catching_materials && scrapy crawl spider_main"
    for key, value in args.items():
        if value is not None:
            cmd += f" -a {key}={shlex.quote(value)}"

    try:
        # Создаем временный файл для логов
        log_file = tempfile.NamedTemporaryFile(delete=False)
        scrapy_logs[user_id] = {
            'log_file': log_file.name,
            'start_time': time.time()
        }

        scrapy_process = subprocess.Popen(
            cmd, shell=True, 
            stdout=log_file,
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid
        )
        
        scrapy_processes[user_id] = scrapy_process
        atexit.register(handle_exit, user_id)
        return jsonify({
            "status": f"Scrapy spider started for user {user_id}.",
            "log_file": f"/scrapy/logs/{user_id}"
        }), 200
    except Exception as e:
        return jsonify({"status": "Error in starting Scrapy spider.", "error": str(e)}), 500

@scrapy_bp.route('/logs/<user_id>', methods=['GET'])
def get_logs(user_id):
    if user_id not in scrapy_logs:
        return jsonify({"status": f"No logs found for user {user_id}."}), 404
    
    log_info = scrapy_logs[user_id]
    
    try:
        # Если процесс еще работает, читаем текущие логи
        if user_id in scrapy_processes and scrapy_processes[user_id].poll() is None:
            with open(log_info['log_file'], 'r') as f:
                content = f.read()
            return jsonify({
                "status": "Logs retrieved (process still running)",
                "logs": content,
                "running": True
            })
        # Если процесс завершен, возвращаем полные логи
        else:
            with open(log_info['log_file'], 'r') as f:
                content = f.read()
            return jsonify({
                "status": "Logs retrieved (process finished)",
                "logs": content,
                "running": False,
                "exit_code": scrapy_processes[user_id].returncode if user_id in scrapy_processes else None
            })
    except Exception as e:
        return jsonify({"status": "Error reading logs", "error": str(e)}), 500

@scrapy_bp.route('/logs-file/<user_id>', methods=['GET'])
def get_logs_file(user_id):
    if user_id not in scrapy_logs:
        return jsonify({"status": f"No logs found for user {user_id}."}), 404
    
    try:
        return send_file(
            scrapy_logs[user_id]['log_file'],
            as_attachment=True,
            download_name=f'scrapy_logs_{user_id}.log',
            mimetype='text/plain'
        )
    except Exception as e:
        return jsonify({"status": "Error sending log file", "error": str(e)}), 500

def handle_exit(user_id):
    if user_id in scrapy_processes:
        scrapy_process = scrapy_processes[user_id]
        if scrapy_process.poll() is None:
            os.killpg(os.getpgid(scrapy_process.pid), signal.SIGTERM)
        
        # Закрываем и удаляем временный файл логов
        if user_id in scrapy_logs:
            try:
                os.unlink(scrapy_logs[user_id]['log_file'])
            except:
                pass
            del scrapy_logs[user_id]
        
        del scrapy_processes[user_id]

@scrapy_bp.route('/stop-scrapy', methods=['POST'])
def stop_scrapy():
    user_id = request.json.get("user_id")
    if user_id not in scrapy_processes or scrapy_processes[user_id].poll() is not None:
        return jsonify({"status": f"No running Scrapy process for user {user_id}."}), 400

    try:
        os.killpg(os.getpgid(scrapy_processes[user_id].pid), signal.SIGTERM)
        
        # Даем процессу немного времени на завершение и запись логов
        time.sleep(1)
        
        # Читаем логи перед удалением
        logs = ""
        if user_id in scrapy_logs:
            with open(scrapy_logs[user_id]['log_file'], 'r') as f:
                logs = f.read()
        
        handle_exit(user_id)
        
        return jsonify({
            "status": f"Scrapy spider stopped for user {user_id}.",
            "logs": logs
        }), 200
    except Exception as e:
        return jsonify({"status": "Error stopping Scrapy spider.", "error": str(e)}), 500