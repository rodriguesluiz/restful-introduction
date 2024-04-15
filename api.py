"""
ATENÇÃO AOS PASSOS PARA EXECUÇÃO:
1. Ativar ambiente virtual: .venv/Scripts/Activate.ps1
2. Inicializar servidor: uvicorn api:app --reload
3. Acessar o servidor: http://127.0.0.1:8000
"""

### IMPORTANDO BIBLIOTECAS ###

# Importa a fastapi
from fastapi import FastAPI
# Modelo de representação de dados usado na fastapi
from pydantic import BaseModel

### HELLO WORLD ###

# Cria o app da nossa api
app = FastAPI()

# A função abaixo lida com requisições que:
# - vão para "/"
# - usam o método 'get'
@app.get("/")
def root():
	return {"message": "Hello World"}










### CRUD ###

# Modelagem dos dados de sorvetes com Pydantic
class Sorvete(BaseModel):
    id: int
    sabor: str

# Dados simulados de sorvetes
# Em um caso real, teríamos uma conexão com um BD
sorvetes = [
    Sorvete(id=1, sabor='Chocolate'),
    Sorvete(id=2, sabor='Morango')
]

# 1. Endpoint para R do CRUD: Recuperar todos os sorvetes
@app.get("/sorvetes/", response_model=list[Sorvete])
def obter_sorvetes():
    return sorvetes

# 2. Endpoint para C do CRUD: Criar um novo sorvete
@app.post("/sorvetes/", response_model=Sorvete)
def adicionar_sorvete(sorvete: Sorvete):
    sorvetes.append(sorvete)
    return sorvete

# 3. Endpoint para U do CRUD: Atualizar (update) um sorvete
@app.put("/sorvetes/{sorvete_id}/", response_model=Sorvete)
def atualizar_sorvete(sorvete_id: int, novo_sorvete: Sorvete):
    for sorvete in sorvetes:
        if sorvete.id == sorvete_id:
            sorvete.sabor = novo_sorvete.sabor
            return sorvete

# 4. Endpoint para D do CRUD: Deletar um sorvete
@app.delete("/sorvetes/{sorvete_id}/")
def excluir_sorvete(sorvete_id: int):
    for i, sorvete in enumerate(sorvetes):
        if sorvete.id == sorvete_id:
            del sorvetes[i]
            return