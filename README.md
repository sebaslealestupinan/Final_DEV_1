ya pana


# Parcial_final

cambie el readme si esta aca

**MODELS**

Jugador_datos_personal{

  nombre:str,
  
  numeroCam:int (numero camisa numero de 1-99), 
  
  year:int (saber edad con el año),
  
  foto (campo opcional enfoquemonos primero que funcione lo demas),
  
  nacionalidad:str (ligas tienen restricciones de jugadores extranjeros)
  
}

Jugador_datos_deportivos{

  altura:float (medida en cm),
  
  peso:float (medida en kg),
  
  pie_dominante:str (izquierdo o derecho),
  
  posicion:str (defensa_centrar y lateral, mediocampo o centrocampo, volantes defensivos, centrales, ofensivos y extremos)
  
  valor_mercado_jugador:int (podemos nombrarla diferente)
  
  year_ingreso_jugador_equipo:int,
  
  estado:str (en el html podemos hacerlo que se elija con un dropdown menu)
  
}

Partido{

  fecha_inicio_partido,

  estadisticas_jugador,
  
  resultado:str (victoria,empate,derrota) si queda en empate de decide por penales
  
}
