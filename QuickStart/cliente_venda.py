import requests


# URL da sua API FastAPI
url = "http://localhost:8000/vendas/"


# Inserir venda usando POST
def criar_venda():
    # Solicita os dados ao usuário
    id_int = int(input("ID da venda: "))
    produto = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    # Monta o dicionário com os dados
    venda = {
        "id_int": id_int,
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade
    }

    # Envia os dados para a API usando POST
    response = requests.post(url, json=venda)
    # Mostra a resposta da API
    print("Status:", response.status_code)
    try:
        print("Resposta:", response.json())
    except Exception:
        print("Resposta (texto):", response.text)


# Ler uma venda usando GET
def ler_venda():
    id_int = input("ID da venda para consultar: ")
    resp = requests.get(url + str(id_int))
    print("Status:", resp.status_code)
    try:
        print("Resposta:", resp.json())
    except:
        print("Resposta (texto):", resp.text)


# Atualizar uma venda usando PUT
def atualizar_venda():
    id_int = input("ID da venda para atualizar: ")
    produto = input("Novo nome do produto: ")
    preco = float(input("Novo preço: "))
    quantidade = int(input("Nova quantidade: "))
    venda = {
        "id_int": int(id_int),
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade
    }
    resp = requests.put(url + str(id_int), json=venda)
    print("Status:", resp.status_code)
    try:
        print("Resposta:", resp.json())
    except:
        print("Resposta (texto):", resp.text)


# Exclui uma venda usando DELETE
def deletar_venda():
    id_int = input("ID da venda para excluir: ")
    resp = requests.delete(url + str(id_int))
    print("Status:", resp.status_code)
    try:
        print("Resposta:", resp.json())
    except:
        print("Resposta (texto):", resp.text)

def menu():
    while True:
        print("\n--- CRUD de Vendas ---")
        print("1. Criar venda")
        print("2. Ler venda")
        print("3. Atualizar venda")
        print("4. Excluir venda")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_venda()
        elif opcao == "2":
            ler_venda()
        elif opcao == "3":
            atualizar_venda()
        elif opcao == "4":
            deletar_venda()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()