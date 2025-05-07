from controller.generation_controller import GenerationController

class GenerationRunner:
    def __init__(self):
        self.controller = GenerationController()

    def execute(self):
        final_audio = self.controller.run_generation()
        if final_audio:
            print(f"Audio generado con éxito: {final_audio}")
        else:
            print("Proceso de generación falló.")