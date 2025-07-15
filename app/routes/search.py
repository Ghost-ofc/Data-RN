from fastapi import APIRouter, Query
from sqlalchemy import text
from database.connection import engine

router = APIRouter()

@router.get("/ping")
def ping():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 'pong'")).fetchone()
            return {"message": result[0]}
    except Exception as e:
        return {"error": str(e)}


@router.get('/dni')
def search_dni(dni: str = Query(...)):
    try:
        with engine.connect() as conn:
            stmt = text("SELECT * FROM personas WHERE dni = :dni")
            result = conn.execute(stmt, {"dni": dni}).mappings().fetchone()
            if result:
                return {"dni": dni, "data": dict(result)}
            else:
                return {"message": "No se encontró el DNI"}
    except Exception as e:
        return {"error": str(e)}