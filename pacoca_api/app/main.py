from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Marca(BaseModel):
    id: int
    nome: str
    origem: str

# Simulando um banco de dados em memória
db = [
    Marca(id=1, nome="Paçoca Amor", origem="São Paulo"),
    Marca(id=2, nome="Paçoquita", origem="Minas Gerais"),
]

@app.get("/marcas/", response_model=List[Marca])
def listar_marcas():
    return db

@app.get("/marcas/{marca_id}", response_model=Marca)
def obter_marca(marca_id: int):
    for marca in db:
        if marca.id == marca_id:
            return marca
    raise HTTPException(status_code=404, detail="Marca não encontrada")

@app.post("/marcas/", response_model=Marca)
def criar_marca(marca: Marca):
    db.append(marca)
    return marca

@app.put("/marcas/{marca_id}", response_model=Marca)
def atualizar_marca(marca_id: int, marca: Marca):
    for idx, m in enumerate(db):
        if m.id == marca_id:
            db[idx] = marca
            return marca
    raise HTTPException(status_code=404, detail="Marca não encontrada")

@app.delete("/marcas/{marca_id}", response_model=Marca)
def deletar_marca(marca_id: int):
    for idx, marca in enumerate(db):
        if marca.id == marca_id:
            db.pop(idx)
            return marca
    raise HTTPException(status_code=404, detail="Marca não encontrada")
