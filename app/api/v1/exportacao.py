from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.connections import get_session
from sqlalchemy import text

router = APIRouter()


@router.get("/exportacao/{ano}")
async def get_exportacao(ano: str, db: Session = Depends(get_session), limit: int = 100, offset: int = 0):
    """
    Returna dados de exportação por ano.
    """
    field_peso: str = f"y{ano}_kg"
    field_dolar: str = f"y{ano}_usd"
    statement: str = f"""SELECT id, pais, {field_peso}, {field_dolar}
                            FROM vitivinicultura.tb_importacao
                           WHERE {field_dolar} > 0 and {field_peso} > 0   
                        ORDER BY {field_dolar}, {field_peso} DESC
                         LIMIT {limit} OFFSET {offset}"""
    results = db.execute(text(statement)).fetchall()
    response = [{"id": row[0], "pais": row[1], "peso": row[2], "dolar": row[3], "ano": ano} for row in results]
    return response
