'''
Juego de dados simple

- Juega un usuario versus la computadora
- Se ingresa la cantidad de partidas a jugar
- Se ingresa un numero del 1 al 6 por teclado
- Se tiran dos dados por lado.

Se suma el valor de ambos y ese es el puntaje obtenido. Este puntaje puede tener un extra:
1- Si uno de los dados coincide con el numero ingresado previamente, se incrementa en 10 el puntaje.
2- si ambos dados son iguales, se multiplica por 10 la suma obtenida.
3- Si son dos valores seguidos (ejemplos: 1-2, 3-4, 4-5) se le agrega al puntaje obtenido el triple del dado de mayor valor.
'''
from random import randint


print("#"*50)
print("Bienvenido al juego de dados")
print("#"*50)

cantidadPartidas = int(input("Ingrese la cantidad de partidas a jugar: "))
partidaActual = 1
lista_partidas = []
while partidaActual <= cantidadPartidas:
  print(":"*50)
  numero = int(input("Ingrese un numero del 1 al 6: "))

  # Definimos los dados al azar
  usuarioDado1 = randint(1,6)
  usuarioDado2 = randint(1,6)
  computadoraDado1 = randint(1,6)
  computadoraDado2 = randint(1,6)

  print(
    f'''
    Sus dados fueron:            {usuarioDado1} - {usuarioDado2}
    Los dados de la computadora: {computadoraDado1} - {computadoraDado2}
    '''
  )

  usuarioPuntaje = usuarioDado1 + usuarioDado2
  computadoraPuntaje = computadoraDado1 + computadoraDado2

  # Verificamos la coincidencia de los dados con el numero
  if usuarioDado1 == numero or usuarioDado2 == numero:
    print("--> Uno de sus dados coincide con el numero! +10")
    usuarioPuntaje = usuarioPuntaje + 10
  if computadoraDado1 == numero or computadoraDado2 == numero:
    print("--> Uno de los dados de la computadora coincide con el numero! +10")
    computadoraPuntaje = computadoraPuntaje + 10

  # Dados de usuario
  if usuarioDado1 == usuarioDado2:
    print(f"--> Tus dados son iguales!!!! + {(usuarioDado1 + usuarioDado2) * 10 }")
    usuarioPuntaje = usuarioPuntaje + (usuarioDado1 + usuarioDado2) * 10
  elif usuarioDado1 > usuarioDado2:
    diferencia = usuarioDado1 - usuarioDado2
    if diferencia == 1:
      # Son consecutivos!!
      print(f"--> Tus dados son consecutivos + {3 * usuarioDado1}")
      usuarioPuntaje = usuarioPuntaje + 3 * usuarioDado1
  else:
    diferencia = usuarioDado2 - usuarioDado1
    if diferencia == 1:
      # Son consecutivos!!
      print(f"--> Tus dados son consecutivos + {3 * usuarioDado2}")
      usuarioPuntaje = usuarioPuntaje + 3 * usuarioDado2

  # Dados de computadora
  if computadoraDado1 == computadoraDado2:
    print(f"--> Los dados de la computadora son iguales!!!! + {(usuarioDado1 + usuarioDado2) * 10 }")
    computadoraPuntaje = computadoraPuntaje + (computadoraDado1 + computadoraDado2) * 10
  elif computadoraDado1 > computadoraDado2:
    diferencia = computadoraDado1 - computadoraDado2
    if diferencia == 1:
      # Son consecutivos!!
      print(f"--> Los dados de la computadora son consecutivos + {3 * computadoraDado1}")
      computadoraPuntaje = computadoraPuntaje + 3 * computadoraDado1
  else:
    diferencia = computadoraDado2 - computadoraDado1
    if diferencia == 1:
      # Son consecutivos!!
      print(f"--> Los dados de la computadora son consecutivos + {3 * computadoraDado2}")
      computadoraPuntaje = computadoraPuntaje + 3 * computadoraDado2
  print(
    f'''
    Resultado Final Partida {partidaActual} / {cantidadPartidas}
    Vos {usuarioPuntaje} Computadora {computadoraPuntaje} 
    '''
  )
  resultado = (usuarioPuntaje, computadoraPuntaje)
  lista_partidas.append(resultado)
  partidaActual=partidaActual+1

# Cantidad de victorias
empate=0
victoria=0
derrota=0
mayorDiferencia = 0
for partida in lista_partidas: # partida --> (puntajeUsuario, puntajePC)
  if partida[0] == partida[1]:
    empate=empate+1
  elif partida[0] > partida[1]:
    victoria=victoria + 1
    if partida[0] - partida[1] > mayorDiferencia:
      mayorDiferencia = partida[0] - partida[1]
  else: 
    derrota = derrota + 1
    if partida[1] - partida[0] > mayorDiferencia:
      mayorDiferencia = partida[1] - partida[0]

print("#"*50)
print(f"{'Estadisticas':^50}")
print("#"*50)

print(
  f'''
  ··· Ganaste: {victoria} partidas
  ··· Perdiste: {derrota} partidas
  ··· Empates: {empate} partidas
  ··· La mayor diferencia en el tanteador fue de {mayorDiferencia}
  '''
)


print("FIN")