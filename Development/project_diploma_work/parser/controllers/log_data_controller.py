from flask import Blueprint, jsonify, request
import os
import time

log_data_bp = Blueprint('log_data', __name__)

@log_data_bp.route('/get-log', methods=['GET'])
def get_log():
    user_id = request.args.get("user_id")
    log_file_path = f"catching_materials/logs/{user_id}_pipeline.log"

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

@log_data_bp.route('/get-data', methods=['GET'])
def get_data():
    user_id = request.args.get("user_id")
    data_file_path = f"catching_materials/data/{user_id}_data.json"

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