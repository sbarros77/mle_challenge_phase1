from fastapi import APIRouter, Depends
from sqlalchemy import column, text
from app.db.connections import get_session
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/producao/{ano}")
async def get_producao_by_id(ano: str, db: Session = Depends(get_session), limit: int = 100, offset: int = 0):
    """
    Retorna dados de producao por ano
    """
    field: str = f"y{ano}"
    statement: str = f"""SELECT id, produto, {field} 
                            FROM vitivinicultura.tb_producao
                           WHERE {field} > 0   
                        ORDER BY produto
                         LIMIT {limit} OFFSET {offset}"""
    results = db.execute(text(statement)).fetchall()
    # Convert to list of dicts for JSON serialization
    response = [{"id": row[0], "produto": row[1], "litros": row[2], "ano": ano} for row in results]
    return response
