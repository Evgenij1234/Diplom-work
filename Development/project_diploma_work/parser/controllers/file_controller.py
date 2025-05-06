import os
from flask import Blueprint, send_from_directory, current_app, jsonify

file_bp = Blueprint('file', __name__, url_prefix='/files')

@file_bp.route('/<username>', methods=['GET'])
def get_scraping_file(username):
    # Базовый путь к проекту (на два уровня выше от app.py)
    base_dir = os.path.dirname(os.path.dirname(current_app.root_path))
    
    # Полный путь к папке с данными
    scraping_dir = os.path.join(
        base_dir,
        'parser',
        'catching_materials',
        'catching_materials',
        'data'
    )
    
    filename = f"{username}_data.json"
    file_path = os.path.join(scraping_dir, filename)
    
    # Для отладки - выведем пути в консоль
    print(f"Base directory: {base_dir}")
    print(f"Looking for file at: {file_path}")
    
    if not os.path.exists(file_path):
        return jsonify({
            "status": "error",
            "message": f"File {filename} not found",
            "expected_path": file_path
        }), 404
    
    return send_from_directory(
        directory=scraping_dir,
        path=filename,
        as_attachment=True,
        mimetype='application/json'
    )