from fastapi import FastAPI, HTTPException
from database import create_db_and_tables
from router import jugador
from contextlib import asynccontextmanager
from models import Jugador, JugadorCreate
from database import SessionDep


app = FastAPI(lifespan=create_tables, title="Sigmotoa FC")

app.include_router(jugador.router, tags=["jugador"], prefix="/jugador")

@app.post("/", response_model=Jugador, status_code=201)
async def create_user(new_jugador:JugadorCreate, session:SessionDep):
    jugador = Jugador.model_validate(new_jugador)
    session.add(jugador)
    session.commit()
    session.refresh(jugador)
    return jugador


@app.get("/{jugador_id}", response_model=Jugador)
async def get_one_jugador(jugador_id:int, session:SessionDep):
    jugador_db = session.get(Jugador, jugador_id )
    if not jugador_db:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return jugador_db

@app.get("/", response_model=list[Jugador])
async def get_all_jugadores(session:SessionDep):
    jugadores = session.query(Jugador).all()
    return jugadores