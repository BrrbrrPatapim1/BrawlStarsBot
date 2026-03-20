import json
import os
import logging

logger = logging.getLogger(__name__)

def load_brawlers():
    if not os.path.exists('data.json'):
        return []  # Виправлено: [] замість {}
    
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error("Помилка: файл data.json пошкоджено або відсутній.")
        return []

def save_brawlers(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    