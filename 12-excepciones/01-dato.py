

while True:
  try:
    edad = int(input("ingrese su edad: "))
    break
  except:
    print("Debes ingresar un numero")

if edad >= 18:
  print("Sos mayor de edad")
else:
  print("sos menor")