from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.connections import get_session
from sqlalchemy import text

router = APIRouter()


@router.get("/comercializacao/{ano}")
async def get_comercializacao(ano: str, db: Session = Depends(get_session), limit: int = 100, offset: int = 0):
    """
    Retorna dados de comercialização por ano.
    """
    field = f"y{ano}"
    statement: str = f"""SELECT id, produto, {field}
                            FROM vitivinicultura.tb_comercializacao
                           WHERE {field} > 0   
                        ORDER BY produto
                         LIMIT {limit} OFFSET {offset}"""
    results = db.execute(text(statement)).fetchall()
    response = [{"id": row[0], "produto": row[1], "quantidade": row[2], "ano": ano} for row in results]
    return response
