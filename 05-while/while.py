"""
El bucle while lo usamos para repetir un bloque de codigo mientras
una condicion sea verdadera, dentro del bloque de codigo en algun momento debera una instruccion hacer falsa la condicion del while para poder salir y evitar un ciclo infinito.


Su sintaxis:

while <condicion>:
  <bloque de codigo>
..........
..........
..........
"""

suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
  suma = suma + numero
  numero = int(input("Ingrese un numero: "))
print("#"*50)
print(f"La suma total es {suma}")
print("#"*50)


