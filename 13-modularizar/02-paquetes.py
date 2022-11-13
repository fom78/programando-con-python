'''
Info: https://docs.python.org/es/3/tutorial/modules.html#packages

Un paquete es una carpeta que contiene varios módulos. Siguiendo nuestro ejemplo , podemos crear el paquete matematica creando una carpeta con ese nombre.

Para indicarle a Python que esa carpeta sera un paquete debemos colocarle dentro un archivo llamado:
__init__.py (Sin contenido)

De la documentacion oficial: "Los archivos __init__.py son obligatorios para que Python trate los directorios que contienen los archivos como paquetes."


Entonces la carpeta matematica dentro tendria: 

- __init__.py
- aritmeticaBasica.py
- aritmeticaCompleja.py

Para acceder a algunos de los modulos y sus funcionalidades pordemos hacerlo de diferentes formas:

- 1
import matematica.aritmeticaBasica

print(matematica.aritmeticaBasica.suma(3, 5))

- 2

from matematica import aritmeticaBasica

print(aritmeticaBasica.resta(7, 5))

- 3

from matematica.aritmeticaCompleja import raiz

print(raiz(7))

'''

from matematicas.aritmeticaCompleja import pot as p, suma as sumaRara
from matematicas.aritmeticaBasica import suma


print(suma(2,3))

print(sumaRara(2,3))

print(p(2,3))