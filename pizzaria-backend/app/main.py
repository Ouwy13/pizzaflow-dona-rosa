from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .routers import produtos, pedidos # Futuros imports dos seus roteadores
# from .database import engine, Base # Futuros imports de conexão com DB

# Isso seria executado apenas para criar as tabelas no banco de dados (geralmente fora do aplicativo principal)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API PizzaFlow Dona Rosa",
    description="Backend para o sistema interno de gestão de pedidos da Pizzaria Dona Rosa.",
    version="0.1.0",
)

# Configuração CORS (Cross-Origin Resource Sharing)
# Permite que seu frontend (hospedado em outro domínio/porta) se conecte ao backend
origins = [
    "http://localhost:3000", # Para desenvolvimento local do frontend
    # Esta URL abaixo será a URL do seu frontend no Vercel após o deploy.
    # Você precisará atualizá-la aqui quando souber a URL final do Vercel.
    "https://pizzaflow-dona-rosa.vercel.app", # Placeholder: Mude para a sua URL real do Vercel!
    # Adicione outras URLs do frontend em produção aqui se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Permite todos os headers
)

# Futuramente, você vai incluir seus roteadores aqui:
# app.include_router(produtos.router, prefix="/api/v1/produtos", tags=["Produtos"])
# app.include_router(pedidos.router, prefix="/api/v1/pedidos", tags=["Pedidos"])

@app.get("/")
async def root():
    return {"message": "API PizzaFlow Dona Rosa está rodando!"}

# Para rodar este backend localmente (futuramente):
# 1. Crie um ambiente virtual: python -m venv venv
# 2. Ative: source venv/bin/activate (Linux/macOS) ou venv\Scripts\activate (Windows)
# 3. Instale dependências: pip install -r requirements.txt
# 4. Rode o servidor: uvicorn app.main:app --reload