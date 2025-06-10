from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em química e física. Responda perguntas sobre estruturas moleculares e suas propriedades."
        },
        {
            "role": "user",
            "content": "CO2 é angular ou linear? Explique de forma simples."
        }
    ],
    max_tokens=150, # Limite de tokens na resposta
    n=1, # Número de respostas a serem geradas      
    temperature=0.7, # Controle de aleatoriedade na resposta, sendo 0 mais conservador e 1 mais criativo.
    top_p=1.0, # Controle de diversidade, 0.1 significa que a resposta será mais focada em palavras mais prováveis, enquanto 1.0 permite uma maior variedade.
    frequency_penalty=1.0, # Se quiser evitar repetições, pode aumentar esse valor, intervalos de 0 a 2.
    presence_penalty=1.0 # Penalidade para introdução de novos tópicos, 0 significa que não há penalidade, enquanto valores maiores incentivam a introdução de novos tópicos. Intervalos de 0 a 2.
)
print(response.choices[0].message.content)