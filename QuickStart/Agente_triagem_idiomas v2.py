from openai import OpenAI
from dotenv import load_dotenv
import os
from agents import Agent, Runner
from QuickStart.agents import Agent, Runner # agents.py

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TriagemIdiomasAgent(Agent):
    def run(self, pergunta, idioma="pt"):
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

# Exemplo de uso com Runner
if __name__ == "__main__":
    pergunta = "Qual é o horário de funcionamento do hospital?"
    idioma = "es"  # espanhol
    agent = TriagemIdiomasAgent() # Cria uma instância do agente de triagem de idiomas 
    runner = Runner(agent) # Cria uma instância do Runner com o agente
    # Executa o agente com a pergunta e o idioma especificados      
    resposta = runner.run(pergunta, idioma)
    print(resposta)