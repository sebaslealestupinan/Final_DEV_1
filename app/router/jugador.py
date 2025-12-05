from app.database_c import SessionDep
from fastapi import APIRouter, HTTPException,Depends
from app.models import Jugador, JugadorCreate


router = APIRouter()

@router.post("/", response_model=Jugador, status_code=201)
async def create_user(new_jugador:JugadorCreate, session:SessionDep):
    jugador = Jugador.model_validate(new_jugador)
    session.add(jugador)
    session.commit()
    session.refresh(jugador)
    return jugador


@router.get("/{jugador_id}", response_model=Jugador)
async def get_one_jugador(jugador_id:int, session:SessionDep):
    jugador_db = session.get(Jugador, jugador_id )
    if not jugador_db:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return jugador_db

@router.get("/", response_model=list[Jugador])
async def get_all_jugadores(session:SessionDep):
    jugadores = session.query(Jugador).all()
    return jugadores

