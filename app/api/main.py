from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.prompt_routes import router as prompt_router
from app.infrastructure.database import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Inicializa recursos compartilhados da aplicacao durante o startup."""
    create_db_and_tables()
    yield


app = FastAPI(
    title="PromptHub AI Python",
    description="API REST para cadastro, analise e priorizacao de prompts de IA.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> dict[str, str]:
    """Retorna o status minimo da aplicacao para smoke checks."""
    return {"status": "ok"}


app.include_router(prompt_router)
