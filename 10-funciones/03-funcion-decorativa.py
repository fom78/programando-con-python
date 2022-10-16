
# Creamos una funcion que realice un decorativo por pantalla 

def decorar():
  print("#"*50)
  print("·"*50) 
  print("#"*50) 

while True:
  decorar()
  print('''
  \t :::Menu:::
  [1] Cargar usuarios
  [2] Mostrar usuarios
  [3] Mostrar listado de trabajadores activos
  [4] Mostrar usuarios por profesion
  [5] Mostrar usuarios por edad
  [0] Salir
  ''')
  decorar()
  opcion = int(input("Seleccione una opcion: "))
  if opcion == 0:
    break
  elif opcion == 1:
    print("Cargar usuarios")
  elif opcion == 2:
    print("Listado usuarios")
  elif opcion == 3:
    print("Trabajadores activos")
  elif opcion == 4:
    print("Busqueda por profesion")
  elif opcion == 5:
    print("Busqueda por edad")
  else:
    print("Ingresa una opcion valida")

print("Fin!!!!")


