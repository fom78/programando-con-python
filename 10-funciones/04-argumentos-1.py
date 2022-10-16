
def saludar(nombre,edad, profesion="Programadora"):
  print(f"Hola {nombre}, tu profesion es: {profesion} y tu edad es {edad}")


'''
Argumento posicionales
Se pueden llamar por su posición en la definición de la función. En este caso el orden en que se pasan es importante.
'''
# saludar("Ingrid", "Estudiante")
# saludar("Fernando","Docente")
# saludar("Estudiante","Ingrid")

'''
Argumentos nombrados
Podemos llamar con argumentos nombrados, sin importar el orden, el resultado será el mismo
'''

# saludar(nombre="Ingrid", profesion="Estudiante")

# saludar(profesion="Estudiante",nombre="Ingrid")

# saludar("Ingrid", "Estudiante",edad=12)

# saludar(nombre="Ingrid", "Estudiante")

# saludar("Estudiante", nombre="Ingrid")

'''
Argumentos opcionales
Los argumentos pueden ser opcionales, para ello el parámetro cuando se define la función debe asignársele un valor predeterminado.

'''
saludar("Ingrid",14)









