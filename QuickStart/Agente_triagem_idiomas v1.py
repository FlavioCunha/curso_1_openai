from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agente_triagem_idiomas(pergunta, idioma="pt"):
    prompt = (
        f"Responda à seguinte pergunta no idioma '{idioma}':\n"
        f"{pergunta}"
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um agente de triagem multilíngue."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Exemplo de uso:
pergunta = "Qual é o horário de funcionamento do hospital?"
idioma = "en"  # espanhol // "en" # inglês
resposta = agente_triagem_idiomas(pergunta, idioma)
print(resposta)