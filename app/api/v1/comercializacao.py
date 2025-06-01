from fastapi import APIRouter

router = APIRouter()


@router.get("/comercializacao")
async def get_comercializacao(limit: int = 100, offset: int = 0):
    """
    Endpoint to retrieve commercial data.
    """
    return {"message": "Comercialização data retrieved successfully."}
