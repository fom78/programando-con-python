

while True:
  try:
    nro1 = float(input("Nro 1 "))
    nro2 = float(input("Nro 2 "))
    res = nro1 / nro2
    break
  except ValueError:
    print("solo admite numeros como ingreso")
  except ZeroDivisionError:
    print("El nro 2 no puede ser cero!!!")
    

print(res)
