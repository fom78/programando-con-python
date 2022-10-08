"""
- La sentencia for de Python itera sobre los ítems de cualquier secuencia o coleccion (una lista o una cadena de texto), en el orden que aparecen en la secuencia

Sintaxis:
for <elemento> in <secuencia>:
  <bloque de codigo>
........
........
........
"""
cadena = "Hola"
for letra in cadena:
  if letra not in "aeiou":
    print(letra, end="")



