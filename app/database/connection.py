from sqlalchemy import create_engine
from app.config.conf import settings


engine = create_engine(settings.DATABASE_URL)

def init_db():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT now()")
            print("✅ Conexión exitosa:", result.fetchone())
    except Exception as e:
        print("❌ Error al conectar:", e)

def close_db():
    try:
        engine.dispose()
        print("🔌 Conexión cerrada correctamente")
    except Exception as e:
        print("❌ Error al cerrar conexión:", e)
