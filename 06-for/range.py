"""
Funcion: Range()
Si se necesita iterar sobre una secuencia de números enteros, es apropiado utilizar la función integrada range(), la cual genera progresiones aritméticas.

range(<fin>) --> Genera una secuencia de numeros desde 0 hasta fin - 1.

range(<inicio>,<fin>) --> Genera una secuencia de numeros desde inicio hasta fin - 1.

range(<inicio>,<fin>, <paso>) --> Genera una secuencia de numeros desde inicio hasta fin - 1 de paso en paso.
"""

for nro in range(0,11,2):
  print(nro, end=" ")
print("Fin!!!")