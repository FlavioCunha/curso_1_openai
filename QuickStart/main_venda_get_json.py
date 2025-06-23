# FastAPI

from fastapi import FastAPI

app = FastAPI()

vendas = {
    "venda1": {
        "id_int": 1, 
        "produto": "Notebook",
        "preco": 2500.00,   
        "quantidade": 5
    },
    "venda2": {
        "id_int": 2,
        "produto": "Smartphone",
        "preco": 1500.00,
        "quantidade": 10
    },
    "venda3": {
        "id_int": 3,
        "produto": "Tablet",
        "preco": 800.00,
        "quantidade": 7
    },
    "venda4": {
        "id_int": 4,
        "produto": "Monitor",
        "preco": 1200.00,
        "quantidade": 3
    }
} 

@app.get("/")
def read_root():
   # return "Minha API está no ar 3.0"
    return { "Vendas": len(vendas)}

@app.get("/vendas/{venda_id}")
def read_vendas(venda_id: str):
    if venda_id not in vendas:
        return {"error": "Venda não encontrada"}
    return vendas [venda_id]

# print(read_vendas("venda2"))

# var_venda = input("Digite o código da venda 1 ou 2 ou 3): ")
# if var_venda == 1 or var_venda == 2 or var_venda == 3:
#     print(read_vendas(f"venda{var_venda}"))
# else:
#     print("Venda não encontrada. Digite 1, 2 ou 3.")

