from fastapi import APIRouter

router = APIRouter()


@router.get("/importacao")
async def get_importacao(limit: int = 100, offset: int = 0):
    """
    Endpoint to retrieve import data.
    """

    return {"message": "Importação data retrieved successfully."}


@router.get("/importacao/{id}")
async def get_importacao_by_id(id: int):
    """
    Endpoint to retrieve import data by ID.
    """
    return {"message": f"Importação data for ID {id} retrieved successfully."}
