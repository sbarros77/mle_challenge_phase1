from fastapi import APIRouter

router = APIRouter()


@router.get("/producao")
async def get_producao(limit: int = 100, offset: int = 0):
    """
    Endpoint to retrieve production data.
    """
    return {"message": "Produção data retrieved successfully."}


@router.get("/producao/{id}")
async def get_producao_by_id(id: int):
    """
    Endpoint to retrieve production data by ID.
    """
    return {"message": f"Produção data for ID {id} retrieved successfully."}
