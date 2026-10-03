from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DadosRaspberry(BaseModel):
    device_id: str
    temperatura: float
    umidade: float
    chuva: float


@app.get("/")
def inicio():
    return {"mensagem": "Servidor funcionando!"}


@app.post("/api/dados")
def receber_dados(dados: DadosRaspberry):
    return {
        "mensagem": "Dados recebidos com sucesso!",
        "dados": dados
    }