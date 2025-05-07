import os
import shutil
from TTS.api import TTS
from config.settings import settings

def download_model(model_name: str):
    print(f"Descargando modelo: {model_name}")
    
    # 1. Descarga (o usa cache si ya está)
    tts = TTS(model_name)
    
    # 2. Construir la ruta manualmente
    user_tts_cache = os.path.expanduser("~/Library/Application Support/tts/")
    model_folder_name = model_name.replace("/", "--")
    model_path = os.path.join(user_tts_cache, model_folder_name)

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No se encontró el modelo descargado en {model_path}")

    # 3. Copiar a /models/
    destination_folder = os.path.join(settings.model_dir, model_folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    print(f"Copiando archivos de {model_path} a {destination_folder}...")

    for file_name in os.listdir(model_path):
        src_file = os.path.join(model_path, file_name)
        dst_file = os.path.join(destination_folder, file_name)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)

    print(f"Modelo '{model_name}' copiado correctamente en {destination_folder}")

if __name__ == "__main__":
    model_name = input("Ingrese el model_name (por ejemplo tts_models/es/mai/tacotron2-DDC): ").strip()
    download_model(model_name)