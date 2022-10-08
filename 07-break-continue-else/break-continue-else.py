'''
La sentencia break, termina el bucle for o while más anidado.

continue, continúa con la siguiente iteración del bucle envolvente más cercano

else se ejecuta cuando es falsa la condicion del while o cuando termina la iteracion del for, si antes encontro un break no se cumple.
'''

for numero in range(6):
  if numero == 2:
    continue
  print(f"numero: {numero}")

print("Fin!")