
continuar = True
while continuar:
  print("""
    1 - Sumar
    2 - Restar
    3 - Salir
  """)
  opcion = int(input("Ingrese opcion: "))

  if opcion == 1:
    print("Sumar")
  elif opcion == 2:
    print("Restar")
  elif opcion == 3:
    print("Salir")
    continuar = False

  else:
    print("Ingrese opcion valida")
