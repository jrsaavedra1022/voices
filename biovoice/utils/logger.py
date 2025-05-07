import logging
import os
from datetime import datetime
from config.settings import settings

def setup_logger(name: str):
    today = datetime.today().strftime('%Y-%m-%d')
    log_folder = os.path.join(settings.log_dir, today)
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "generation.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)

    return logger