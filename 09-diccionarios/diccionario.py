
'''
Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.
'''

# creamos un diccionario vacio

dic1 = {}
dic1 = dict()

# creamos diccionario con los elementos 

'''
dic1 = {
  "cuadrado": 4,
  "triangulo": 3,
  "rectangulo": 4,
  "hexagono": 6,
  "pentagono": 5,
  "rombo": 4,
}

'''
dic1 = {
  "cuadrado": 4,
  "triangulo": 3,
  "rectangulo": 4,
  "hexagono": 6,
  "pentagono": 5,
  "rombo": 4,
}

'''creamos un diccionario mediante una coleccion, para esto
necesitamos tener una coleccion que contenga como elementos otra coleccion de pares.
'''

# coleccion=[(1,2),(33,87),("Hola",True)]
# print(coleccion)
# dic1 = dict(coleccion)

# Obtener un valor segun su clave

# print(dic1["hexagono"])

# Modificar un valor segun su clave 

dic1["hola"]=235

dic1.update({"chau":34,37:12, "rombo":5})
# print(dic1["hexagono"])
# Eliminar un elemento segun su clave dic.pop(key)

# dic1.pop("hello")

print(dic1)