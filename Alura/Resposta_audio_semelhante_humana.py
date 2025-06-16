from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Obtenha a resposta em texto
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user",
         "content": "Responda em português: Um golden retriever é um bom cachorro para família?"}
    ]
)

text = response.choices[0].message.content

# Imprime a resposta em texto
print(text)


# 2. Envie o texto para o endpoint de TTS (Text-to-Speech)
audio_response = client.audio.speech.create(
    model="tts-1-hd",  # ou "tts-1"
    voice="alloy",
    input=text
)

# 3. Salve o áudio retornado
with open("dog.wav", "wb") as f:
    f.write(audio_response.content)