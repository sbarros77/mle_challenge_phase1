from fastapi import APIRouter

router = APIRouter()


@router.get("/processamento")
async def get_processamento(limit: int = 100, offset: int = 0):
    """
    Endpoint to retrieve processing data.
    """
    return {"message": "Processamento data retrieved successfully."}


@router.get("/processamento/{id}")
async def get_processamento_by_id(id: int):
    """
    Endpoint to retrieve processing data by ID.
    """
    return {"message": f"Processamento data for ID {id} retrieved successfully."}
