

cadena = "Hola Mundo una nueva clase estamos viendo"

for letra in cadena:
  if letra == "a":
    veces = cadena.count(letra)
    print(f"Letra encontrada y esta presente {veces} veces")
    break
else:
  print("Letra no encontrada")

print("Fin")