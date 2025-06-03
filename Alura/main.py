from openai import OpenAI
from dotenv import load_dotenv # pacote
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Corrigido para usar OpenAI diretamente

resposta = cliente.chat.completions.create(
    messages=[
        {"role": "system", "content": "Listar apenas o nome do produto sem descrição"},

        {"role": "user", "content": "Liste 4 produtos sustentáveis"}
    ],
    model="gpt-4"
)

print(resposta.choices[0].message.content) # Exibindo a resposta da API