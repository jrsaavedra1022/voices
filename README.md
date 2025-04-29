# Proyecto para convertir texto a audio con TTS

## Crear ambiente virtual

- El sistema funciona con python 3.11

```shell
    brew install python@3.11
```

- Crear entorno virtual

```shell
/opt/homebrew/opt/python@3.11/libexec/bin/python3 -m venv venv-tts
source venv-tts/bin/activate
```

## Instalar los requerimientos

```shell
pip3 install -r requirements.txt
```

## Ejecutar el archivo

- Verificar el archivo `src/config/settings.py` y crear un archivo `.env`con las configuraciones necesarias.
- Utilizar el archivo `src/download_model.py` para descargar los modelos necesarios.
- Realizar la ejecución del proyecto

```shell
python3 src/main.py
```