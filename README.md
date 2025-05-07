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

- Verificar el archivo `biovoice/config/settings.py` y crear un archivo `.env`con las configuraciones necesarias.
- Utilizar el archivo `biovoice/download_model.py` para descargar los modelos necesarios.
- Realizar la ejecución del proyecto

```shell
python3 biovoice/app.py 
```

 - Se lo ejecutas por sh configura los archivos .env

```shell
chmod +x run_with_voice.sh
bash run_with_voice.sh carlos
```