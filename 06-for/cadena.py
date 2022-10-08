
cadena = input("Ingrese una cadena: ")

vocales = 0

for letra in cadena:
  if letra in "aeiou":
    vocales += 1

print(f"La cantidad de vocales en la cadena es de {vocales}")



