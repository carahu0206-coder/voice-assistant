# Voice Assistant (v0.1)

This is a simple AI voice assistant project.

## What it can do
- Open applications using voice commands
  - e.g. "Open WeChat"

## Why I built this
I am currently learning AI engineering and building small practical projects.

## Next steps
- Add more commands
- Integrate LLM for smarter understanding

## Model

This project uses a local LLM via Ollama.

Example model:
- qwen3:0.6b

Make sure you install Ollama and pull the model before running.

## Speech Recognition Model (Vosk)

This project uses an offline speech recognition engine based on Vosk.

👉 Vosk: https://alphacephei.com/vosk/models

### Model Setup

1. Download a model from:
   https://alphacephei.com/vosk/models
   Example:
   - vosk-model-small-cn-0.22 (Chinese)
   - vosk-model-small-en-us-0.15 (English)
2. Extract the model to your local directory
3. Update the model path in code:
```python
model_path = r"your/local/path/to/vosk-model"
model = vosk.Model(model_path)

## How to run

1. Install Ollama and start it
2. Pull the model:
   ollama run llama3

3. Run the script:
   python main.py