# creamos una tupla vacia
tupla=()
tupla=tuple()
# creamos la tupla con los elementos
tupla = ("Hola", 1.4,78,[10,20,30],False,78)
# También pueden declararse sin (), separando por , todos sus elementos.
tupla = "Hola", 1.4,78,[10,20,30],False,78

# creamos una tupla partiendo de una cadena de caracteres
# tupla = tuple("Hola")

# # creamos una tupla segun un rango dado
# tupla = tuple(range(5))

print(tupla)

'''
Para acceder a ver el contenido de una tupla lo realizamos de manera similar a las listas o strings indicando entre corchetes su posicion

tupla[posicion]
'''
tupla[2] = 34
print(tupla[2])