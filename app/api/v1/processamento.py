from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.connections import get_session

router = APIRouter()


@router.get("/processamento/{ano}")
async def get_processamento(ano: str, db: Session = Depends(get_session), limit: int = 100, offset: int = 0):
    """
    Retorna dados de processamento de uvas e vinhos.
    """
    field: str = f"y{ano}"
    statement: str = f"""SELECT id, cultivar, {field} 
                           FROM vitivinicultura.tb_processamento
                          WHERE {field} > 0   
                       ORDER BY cultivar
                        LIMIT {limit} OFFSET {offset}"""

    result = db.execute(text(statement)).fetchall()
    response = [{"id": row[0], "cultivar": row[1], "quantidade": row[2], "ano": ano} for row in result]
    return response
