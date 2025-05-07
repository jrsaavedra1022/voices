#!/bin/bash

# run_with_voice.sh - Set env for selected voice and run the app.
# Usage: bash run_with_voice.sh ana

VOICE="$1"
ENV_DIR=".envs"
ENV_FILE="$ENV_DIR/${VOICE}.env"

if [ -z "$VOICE" ]; then
  echo "Please specify a voice. Usage: bash run_with_voice.sh ana"
  exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
  echo "Environment file '$ENV_FILE' not found."
  exit 1
fi

echo "Setting environment for voice: $VOICE"
cp "$ENV_FILE" .env

echo "Activating virtual environment..."
source venv-tts/bin/activate

echo "Running app with voice: $VOICE"
python3 biovoice/app.py