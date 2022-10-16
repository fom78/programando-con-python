'''
Juego de dados simple

Juega un usuario versus la computadora
Se ingresa un numero del 1 al 6 por teclado
Se tiran dos dados por lado.

Se suma el valor de ambos y ese es el puntaje obtenido. Este puntaje puede tener un extra:
1- Si uno de los dados coincide con el numero ingresado previamente, se incrementa en 10 el puntaje.
2- si ambos dados son iguales, se multiplica por 10 la suma obtenida.
3- Si son dos valores seguidos (ejemplos: 1-2, 3-4, 4-5) se le agrega al puntaje obtenido el triple del dado de mayor valor.
'''

from random import randint


numero = int(input("Ingrese un numero(1-6): ")) # 3

dado1 = randint(1,6) # 5
dado2 = randint(1,6) # 3

dadoPc1 = randint(1,6) # 5
dadoPc2 = randint(1,6) # 3

puntaje = dado1 + dado2

puntajePc = dadoPc1 + dadoPc2

if dado1 == numero or dado2 == numero: # Falso or True --> True
  puntaje = puntaje + 10

if dado1 == dado2:
  puntaje = puntaje + (dado1 + dado2) * 10
elif dado1 > dado2: # 5 3 - 5 4
  diferencia = dado1 - dado2
  if diferencia == 1:
    # Son consecutivos
    puntaje = puntaje + dado1*3
else:
  diferencia = dado2 - dado1
  if diferencia == 1:
    # Son consecutivos
    puntaje = puntaje + dado2*3

# Evaluacion para PC
if dadoPc1 == numero or dadoPc2 == numero: 
  puntajePc = puntajePc + 10

if dadoPc1 == dadoPc2:
  puntajePc = puntajePc + (dadoPc1 + dadoPc2) * 10
elif dadoPc1 > dadoPc2: # 5 3 - 5 4
  diferencia = dadoPc1 - dadoPc2
  if diferencia == 1:
    # Son consecutivos
    puntajePc = puntajePc + dadoPc1*3
else:
  diferencia = dadoPc2 - dadoPc1
  if diferencia == 1:
    # Son consecutivos
    puntajePc = puntajePc + dadoPc2*3


print(
  f'''
  Sus dados son : {dado1} - {dado2}
  Dados de la PC: {dadoPc1} - {dadoPc2}
  '''
)

if puntaje > puntajePc:
  print(f" Ganaste!!!! {puntaje} a {puntajePc}")
elif puntaje < puntajePc:
  print(f" Perdiste {puntajePc} a {puntaje}")
else:
  print(f"Empate!!! en {puntaje}")




