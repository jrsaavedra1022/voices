import os
from datetime import datetime
from config.settings import settings
from utils.logger import setup_logger
from utils.file_utils import read_paragraphs_from_txt, save_paragraphs_to_json
from utils.progress_bar import progress_bar
from utils.text_splitter import split_text_into_sentences   
from tts.tts_service import TTSService
from audio.audio_manager import AudioManager

logger = setup_logger(__name__)

def main():
    logger.info("Inicio del proceso de generación de audio.")

    # 1. Buscar archivo .txt en input
    txt_files = [f for f in os.listdir(settings.input_dir) if f.endswith('.txt')]
    if not txt_files:
        logger.error("No se encontró ningún archivo .txt en la carpeta de entrada.")
        return

    txt_path = os.path.join(settings.input_dir, txt_files[0])
    paragraphs = read_paragraphs_from_txt(txt_path)

    # 2. Guardar párrafos en JSON
    json_output = save_paragraphs_to_json(paragraphs)
    logger.info(f"Párrafos guardados en: {json_output}")

    # 3. Inicializar TTS y AudioManager
    tts_service = TTSService()
    audio_manager = AudioManager()

    today = datetime.today().strftime('%Y-%m-%d')
    audio_temp_dir = os.path.join(settings.audio_output_dir, today)
    os.makedirs(audio_temp_dir, exist_ok=True)

    audio_files = []

    # 4. Generar audios individuales
    for index, paragraph in progress_bar(enumerate(paragraphs, start=1), total=len(paragraphs), description="Generando audios"):
        sentences = split_text_into_sentences(paragraph)

        for sub_index, sentence in enumerate(sentences, start=1):
            output_audio = os.path.join(audio_temp_dir, f"audio_{index}_{sub_index}.wav")
            tts_service.generate_audio(sentence, output_audio)
            audio_files.append(output_audio)

    # 5. Combinar audios
    final_audio_path = os.path.join(audio_temp_dir, f"{today}-{settings.voice}.wav")
    audio_manager.combine_audios(audio_files, final_audio_path)

    # 6. Limpiar audios individuales
    audio_manager.delete_temp_audios(audio_files)

    logger.info(f"Proceso finalizado. Audio final generado en: {final_audio_path}")

if __name__ == "__main__":
    main()