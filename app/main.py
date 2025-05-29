from fastapi import FastAPI, APIRouter
from pathlib import Path
import yaml
from controllers import (
    auth_controller, 
    producao_controller, 
    processamento_controller,
    comercializacao_controller,
    importacao_controller,
    exportacao_controller
) 

# Carrega o YAML
def load_openapi():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    # DATA_DIR = BASE_DIR / "fastapi-embrapa"
    DATA_DIR = BASE_DIR / "fastapi-embrapa"

    with open(DATA_DIR / "openapi.yaml", encoding='utf-8') as f:
        return yaml.safe_load(f)

app = FastAPI(
    title="API EMBRAPA",
    description="API para gerenciar Produção, Processamento, Comercialização, Importação e Exportação.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# roteador principal
API_PREFIX = "/api/v1"
main_router = APIRouter(prefix=API_PREFIX)

# Mescla a especificação YAML com as rotas
app.openapi_schema = load_openapi()

# Incluir os outros roteadores no roteador principal
main_router.include_router(auth_controller.router, prefix="/auth")
main_router.include_router(producao_controller.router)
main_router.include_router(processamento_controller.router)
main_router.include_router(comercializacao_controller.router)
main_router.include_router(importacao_controller.router)
main_router.include_router(exportacao_controller.router)

# Incluir o roteador principal no app
app.include_router(main_router)