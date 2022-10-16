print("Bucles!!")

# while
# nro=0
# while nro <= 4: # 4 9 58
#   print("Dentro del bucle")
#   nro = nro + 1
#   print("Hola")

# print("FIN")

# for
# Una cadena es iterable

'''cadena = "Hola"

for letra in "Sobre":
  print("dentro del bucle")
  print(letra)
  print(letra in "Solo")
  
print("Fin!!!")
'''

# range(inicio, fin, paso) --->> range(55) -->> 0,1,...54
# range(23,55,4) --> 23,27,31,..... 52
# print(type(range(23,55,4)))

# for x in range(4): # range(4) -->> 0 1 2 3
#   print("Hola mundo",x)

x = 0
while True:
  print(f"Hola!! {x}")
  x = x + 1
  
  if x == 2:
    print("AAA")
    continue
  if x == 4:
    break
  

print("Fin")





