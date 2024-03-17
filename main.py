from fastapi import FastAPI

app = FastAPI()

# Rota inicial
@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de marcas de paçoca!"}
