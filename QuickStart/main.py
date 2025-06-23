# Exemplo prático em Python usando FastAPI para criar a API e o pymongo para inserir no MongoDB. O fluxo será:
# Usuário informa os dados da venda (produto, preço, quantidade) via uma requisição para a API.
# A API recebe os dados e salva no MongoDB.
# Instalação dos pacotes necessários: pip install fastapi[all] pymongo

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.responses import JSONResponse


app = FastAPI()

# Conectando ao MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["Teste_API"]
collection = db["Vendas"]

# Modelo de venda para validação dos tipos de dados
class Venda(BaseModel):
    id_int: int
    produto: str
    preco: float
    quantidade: int

# POST para criar uma nova venda
@app.post("/vendas/")
def criar_venda(venda: Venda):
    venda_dict = venda.dict()
    venda_obj = {
        f"venda{venda_dict['id_int']}": venda_dict
    }
    try:
        result = collection.insert_one(venda_obj)
        return {
            "msg": "Venda inserida com sucesso!",
            "dados": venda_dict,
            "id_mongo": str(result.inserted_id)
    }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"erro": str(e)}
        )
    
# GET para listar uma venda especifica pelo ID
@app.get("/vendas/{id_int}")
def get_venda(id_int: int):
    venda = collection.find_one({f"venda{id_int}.id_int": id_int})
    if venda:
        # Remove o ObjectId do retorno (pois não é serializável)
        venda.pop("_id", None)
        return venda
    raise HTTPException(status_code=404, detail="Venda não encontrada")


# PUT para atualizar uma venda
@app.put("/vendas/{id_int}")
def update_venda(id_int: int, venda: Venda):
    filter_ = {f"venda{id_int}.id_int": id_int}
    new_values = {
        "$set": {
            f"venda{id_int}": venda.dict()
        }
    }
    result = collection.update_one(filter_, new_values)
    if result.matched_count:
        return {"msg": "Venda atualizada com sucesso!"}
    else:
        raise HTTPException(status_code=404, detail="Venda não encontrada para atualizar")


# DELETE para remover uma venda
@app.delete("/vendas/{id_int}")
def delete_venda(id_int: int):
    filter_ = {f"venda{id_int}.id_int": id_int}
    result = collection.delete_one(filter_)
    if result.deleted_count:
        return {"msg": "Venda removida com sucesso!"}
    else:
        raise HTTPException(status_code=404, detail="Venda não encontrada para excluir")
