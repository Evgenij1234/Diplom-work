from flask import Blueprint, jsonify, request
import subprocess
import shlex
import os
import signal
import atexit

scrapy_bp = Blueprint('scrapy', __name__)
scrapy_processes = {}

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
        scrapy_process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, preexec_fn=os.setsid
        )
        scrapy_processes[user_id] = scrapy_process
        atexit.register(handle_exit, user_id)
        return jsonify({"status": f"Scrapy spider started for user {user_id}."}), 200
    except Exception as e:
        return jsonify({"status": "Error in starting Scrapy spider.", "error": str(e)}), 500

def handle_exit(user_id):
    if user_id in scrapy_processes:
        scrapy_process = scrapy_processes[user_id]
        if scrapy_process.poll() is None:
            os.killpg(os.getpgid(scrapy_process.pid), signal.SIGTERM)
        del scrapy_processes[user_id]

@scrapy_bp.route('/stop-scrapy', methods=['POST'])
def stop_scrapy():
    user_id = request.json.get("user_id")
    if user_id not in scrapy_processes or scrapy_processes[user_id].poll() is not None:
        return jsonify({"status": f"No running Scrapy process for user {user_id}."}), 400

    try:
        os.killpg(os.getpgid(scrapy_processes[user_id].pid), signal.SIGTERM)
        del scrapy_processes[user_id]
        return jsonify({"status": f"Scrapy spider stopped for user {user_id}."}), 200
    except Exception as e:
        return jsonify({"status": "Error stopping Scrapy spider.", "error": str(e)}), 500