from fastapi import FastAPI

from app.api.v1 import comercializacao, exportacao, importacao, processamento, producao, management

app = FastAPI(
    title="Embrapa vinicultura API",
    description="API para gerenciar o processamento de dados de importação, comercialização e outros.",
    version="1.0.0",
)

app.include_router(processamento.router, prefix="/api/v1", tags=["Processamento"])
app.include_router(importacao.router, prefix="/api/v1", tags=["Importação"])
app.include_router(comercializacao.router, prefix="/api/v1", tags=["Comercialização"])
app.include_router(exportacao.router, prefix="/api/v1", tags=["Exportação"])
app.include_router(producao.router, prefix="/api/v1", tags=["Produção"])
app.include_router(management.router, prefix="/api/v1", tags=["Management"])


@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "API is running successfully."}
