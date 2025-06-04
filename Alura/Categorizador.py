from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

modelo = "gpt-4" # Modelo de linguagem a ser utilizado

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    prompt_sistema = f"""
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas
    {lista_categorias_possiveis.split(",")}

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: Apresentar a categoria do produto

    # Exemplo da Saída
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos verdes

    """
    resposta = cliente.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": nome_produto}
        ],
        model= modelo,
        temperature = 1, # What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        max_tokens= 200 # quantidade de tokens gerados
    #   n=3 # Quantidade de respostas geradas
    )

    return resposta.choices[0].message.content

categorias_validas = "Moda Sustentável, Produtos para o Lar, Beleza Natural, Eletrônicos Verdes, Higiene Pessoal"

while True:
    nome_produto = input("Digite o nome do produto: ")
    if nome_produto == "sair" or nome_produto == "Sair"
        print("Até breve...")
        break
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)
    print(texto_resposta)
