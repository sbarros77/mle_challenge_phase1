from typing import Optional
from fastapi import APIRouter

router = APIRouter()


@router.post("/load_data/{load_type}")
async def load_data(load_type: Optional[str]):
    """
    Endpoint to load data based on the specified load type.

    Args:
        load_type (str): The type of data to load (e.g., 'importacao', 'comercializacao').

    Returns:
        dict: A message indicating the status of the data loading process.
    """
    if not load_type:
        return {"message": "Loading all data."}

    return {"message": f"Data loading for {load_type} initiated."}
