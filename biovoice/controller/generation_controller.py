import os
from datetime import datetime
from config.settings import settings
from utils.logger import setup_logger
from utils.file_utils import read_paragraphs_from_txt, save_paragraphs_to_json
from utils.progress_bar import progress_bar

from text.text_service import TextService
from tts.tts_service import TTSService
from audio.audio_manager import AudioManager

logger = setup_logger(__name__)

class GenerationController:
    def __init__(self):
        self.text_service = TextService()
        self.tts_service = TTSService()
        self.audio_manager = AudioManager()

    def run_generation(self):
        logger.info("Iniciando generación de audio...")

        # 1. Buscar archivo
        txt_files = [f for f in os.listdir(settings.input_dir) if f.endswith('.txt')]
        if not txt_files:
            logger.error("No se encontró ningún archivo .txt en la carpeta de entrada.")
            return None

        txt_path = os.path.join(settings.input_dir, txt_files[0])
        paragraphs = read_paragraphs_from_txt(txt_path)

        # 2. Mejora de puntuación
        enhanced_paragraphs = self.text_service.enhance_paragraphs(paragraphs)

        # 3. Guardar JSON
        json_path = save_paragraphs_to_json(enhanced_paragraphs)
        logger.info(f"Párrafos guardados en: {json_path}")

        # 4. Preparar carpetas
        today = datetime.today().strftime('%Y-%m-%d')
        temp_dir = os.path.join(settings.audio_output_dir, today)
        os.makedirs(temp_dir, exist_ok=True)

        # 5. Generar audios
        audio_files = []
        for idx, paragraph in progress_bar(enumerate(enhanced_paragraphs, start=1), total=len(enhanced_paragraphs), description="Generando audios"):
            sentences = self.text_service.split_sentences(paragraph)
            for sidx, sentence in enumerate(sentences, start=1):
                output_audio = os.path.join(temp_dir, f"audio_{idx}_{sidx}.wav")
                self.tts_service.generate_audio(sentence, output_audio)
                audio_files.append(output_audio)

        # 6. Combinar y mejorar audio
        final_audio = os.path.join(temp_dir, f"{today}-{settings.voice}.wav")
        self.audio_manager.combine_audios(audio_files, final_audio)
        self.audio_manager.enhance_audio(final_audio)

        # 7. Limpiar temporales
        self.audio_manager.delete_temp_audios(audio_files)

        logger.info(f"Audio final generado en: {final_audio}")
        return final_audio