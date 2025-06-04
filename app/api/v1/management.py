from fastapi import APIRouter
from app.services.embrapa.downloader import download_all
router = APIRouter()


@router.post("/load_all_data/")
async def load_data_all_data():
    """
    Download e carrega todos os dados do site da Embrapa Vinho para o banco de dados.
    """
    statuses = download_all()
    return {"status": "Dados carregados com sucesso", "details": statuses}
