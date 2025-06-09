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
    max_tokens=150,
    n=1,
    temperature=0.7,
    top_p=1.0,
    frequency_penalty=1.0,
    presence_penalty=1.0
)

print(response.choices[0].message.content)
