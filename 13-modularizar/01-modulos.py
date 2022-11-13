'''
info oficial: https://docs.python.org/es/3/tutorial/modules.html#

Un módulo es un archivo de Python cuyos objetos (funciones, variables, constantes, etc.) pueden ser accedidos desde otro archivo. De esta forma podemos organizar grandes códigos.


Un ejemplo, un archivo aritmeticaBasica.py que contenga lo siguiente.


def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  return a / b



Para acceder a estas funciones desde otro archivo python, podemos realizarlo de difrentes maneras

import aritmeticaBasica

print(aritmeticaBasica.suma(2, 3))



from aritmeticaBasica import suma

print(suma(4, 8))


Para acelerar la carga de módulos, Python cachea las versiones compiladas de cada módulo en el directorio __pycache__ bajo el nombre module.version.pyc

'''

from aritmeticaBasica import suma, resta

print(resta(2,3))