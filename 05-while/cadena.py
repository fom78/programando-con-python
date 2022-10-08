
cadena = input("Ingrese una cadena: ")

longitud=len(cadena)
indice = 0
vocales = 0
while indice < longitud: # 0 4
  if cadena[indice] in "aeiou":
    vocales = vocales + 1
  indice = indice + 1
print(f"La cantidad de vocales en la cadena es de {vocales}")



