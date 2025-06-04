import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

# Obter a data e hora atual
data_hora_atual = datetime.now()
# Formatar a data e hora
data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


def analisador_sentimentos(produto):
    prompt_sistema = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 100 palavras resumindo as avaliações e 
        depois atribua qual o sentimento geral para o produto.
        Identifique também 2 pontos fortes e 2 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com dois bullets
        Pontos fracos: lista com dois bullets
    """
    prompt_usuario = carrega(f"./dados/avaliacoes-{produto}.txt")
    print(f"Iniciou a análise de sentimentos do produto {produto} - {data_hora_formatada}")

    lista_mensagens = [
    {
    "role": "system",
    "content": prompt_sistema
    },
    {
    "role": "user",
    "content": prompt_usuario
    }
    ]

    try:
        resposta = cliente.chat.completions.create(
                    messages = lista_mensagens,
                    model=modelo
            )

        texto_resposta = resposta.choices[0].message.content

    except openai.APIError as e:
        print(f"Erro de API: {e}")
    
    except openai.AuthenticationError as e:
        print(f"Erro de Autenticação: {e}")

    salva(f"./dados/analise-{produto}.txt", texto_resposta)
    print(f"Finalizou a análise de sentimentos do produto {produto} - {data_hora_formatada}")

lista_de_produtos = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados"]

for um_produto in lista_de_produtos:
    analisador_sentimentos(um_produto)

