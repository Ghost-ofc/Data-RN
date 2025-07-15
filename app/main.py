from fastapi import FastAPI
from config.conf import settings
from routes.search import router
from database.connection import init_db, close_db
import uvicorn

def lifespan(app: FastAPI):
    init_db()
    yield
    close_db()


app = FastAPI(lifespan=lifespan)


app.include_router(router, prefix="/search")

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, reload=True)