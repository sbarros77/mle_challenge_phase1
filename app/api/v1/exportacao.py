from fastapi import APIRouter

router = APIRouter()


@router.get("/exportacao")
async def get_exportacao(limit: int = 100, offset: int = 0):
    """
    Endpoint to retrieve export data.
    """
    return {"message": "Exportação data retrieved successfully."}


@router.get("/exportacao/{id}")
async def get_exportacao_by_id(id: int):
    """
    Endpoint to retrieve export data by ID.
    """
    return {"message": f"Exportação data for ID {id} retrieved successfully."}
