

# creamos una lista vacia
lista=[]
lista=list()
# creamos la lista con los elementos
lista = ["Hola", 1.4,78,[10,20,30],False,78]

# creamos una lista partiendo de una cadena de caracteres
lista = list("Hola")

# creamos una lista segun un rango dado
lista = list(range(5))

lista = ["Hola", 1.4,78,[10,20,30],False,78]
# Acceder a ver el contenido de un elemento por indice
# lista[1]="Hola"
# print(lista[1])
"""
Modificando y obteniendo elementos
# Para modificar el contenido en una posicion accedemos con los []
lista[3] = 34

si queremos saber el indice de un elemento:
["pera","naranja","manzana","uva"].index("naranja")

Cuando obtenemos un elemento accediendo por su indice nos retornara un dato que sera del tipo de dato de ese elemento.

Cuando obtenemos una rebanada siempre nos dara como resultado una lista, asi sea de longitud 1.

# lista = ["Hola", 1.4,78,[10,20,30],False,78]


lista = ["Hola", 1.4,78,[10,20,30],False,78]
var1 = lista[0:3] # Tipo list
var2 = lista[:4] # Tipo list
var3 = lista[4:5] # Tipo list

print(f"Los Tipos: \nvar1 es {type(var1)} : {var1}\nvar2 es {type(var2)} : {var2}\nvar3 es {type(var3)} : {var3}")

"""
var = lista[0] # Tipo str
var = lista[4] # Tipo bool
var = lista[3] # Tipo list

# print(lista[4:5])

'''
Agregando elementos a la lista


- Append() agrega un elemento al final de la lista
- Extend() agrega una lista a otra
- Insert() agrega un elemento en una posicion especifica y desplaza el resto de la lista

'''
lista.append(234)
lista.append(23)
lista.insert(2,"Chau")
lista.extend([10,20,40,99,"Hola"])

'''
Eliminando elementos en la lista
- Pop() elimina el ultimo elemento de la lista o el elemento cuyo
indice se le pasa como parametro
- Remove() elimina el elemento que se le pasa como parametro
- clear() elimina todos los elementos de la lista
'''
# lista.remove("Hola")
# lista = [1, 2, 3, 4, 45, 66, 7,5,4,5, 8, 9, 10]

# count() cuenta las repeticiones de un elemento
# print(lista.count(4))
# print(lista.count(7898))
# concatenar +
# print(lista+[2,"hola"])

lista1 = [1,2] + ["hola", True]
print(len(lista))
#longitud de la lista


# Pertenencia

print(2 in lista1)
print(lista)

