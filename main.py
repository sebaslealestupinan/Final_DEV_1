from fastapi import FastAPI
from database import create_tables
from router import jugador
from contextlib import asynccontextmanager

@asynccontextmanager
async def life(app:FastAPI):
    create_tables()
    print("base de datos funcional.")
    yield
app = FastAPI(lifespan=create_tables, title="Sigmotoa FC")

app.include_router(jugador.router, tags=["jugador"], prefix="/jugador")