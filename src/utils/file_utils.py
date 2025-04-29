import os
import json
from datetime import datetime
from config.settings import settings

def read_paragraphs_from_txt(file_path: str) -> list:
    paragraphs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Ignorar líneas vacías
                paragraphs.append(line)
    return paragraphs

def save_paragraphs_to_json(paragraphs: list):
    today = datetime.today().strftime('%Y-%m-%d')
    output_folder = os.path.join(settings.json_dir, today)
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "paragraphs.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(paragraphs, f, ensure_ascii=False, indent=4)
    return output_path