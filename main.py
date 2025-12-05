from fastapi import FastAPI
from database import create_tables
from router import jugador

app = FastAPI(lifespan=create_tables, title="Sigmotoa FC")

app.include_router(jugador.router, tags=["jugador"], prefix="/jugador")

