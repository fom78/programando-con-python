dic1 = {
  "cuadrado": 4,
  "triangulo": 3,
  "rectangulo": 4,
  "hexagono": 6,
  "pentagono": 5,
  "rombo": 4,
}


# Iterar por la clave
'''
- Se itera sobre el metodo keys(), este puede omitirse e igualmente va a iterar por clave
for clave in dic1.keys():
  print(clave)
'''
# for clave in dic1.keys():
#   print(clave, dic1[clave])

# Iterar por el valor
'''
- Se itera sobre el metodo values()

for valor in dic1.values():
  print(valor)
'''

# Iterar por clave y valor
'''
- Se itera sobre el metodo items()

for clave, valor in dic1.items():
  print(clave, valor)
'''
for pepito, valor in dic1.items():
  print(pepito, valor)