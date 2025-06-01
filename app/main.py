from fastapi import FastAPI

from app.api import v1

app = FastAPI(
    title="Embrapa vinicultura API",
    description="API para gerenciar o processamento de dados de importação, comercialização e outros.",
    version="1.0.0",
)

app.include_router(v1.processamento.router, prefix="/api/v1", tags=["Processamento"])
app.include_router(v1.importacao.router, prefix="/api/v1", tags=["Importação"])
app.include_router(
    v1.comercializacao.router, prefix="/api/v1", tags=["Comercialização"]
)
app.include_router(v1.exportacao.router, prefix="/api/v1", tags=["Exportação"])
app.include_router(v1.producao.router, prefix="/api/v1", tags=["Produção"])
app.include_router(v1.management.router, prefix="/api/v1", tags=["Management"])


@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "API is running successfully."}
