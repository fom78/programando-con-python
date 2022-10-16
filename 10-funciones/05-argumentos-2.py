'''
Los argumentos se pueden pasar por valor (una copia de la variable) o por referencia (la direccion de memoria)

Por valor seran los datos simples como los str int float o bool

Por referencia cualquier coleccion, como las listas, diccionarios, etc, y se trabajara con esa variable dentro de la funcion.

'''

# Argumento por valor

# def doblarNumero(nro):
#   nro = nro * 2
#   return nro

# miNumero = 3
# print(doblarNumero(miNumero)) # 6
# print(miNumero) # 3 --> No se modifica el valor

# Argumento por referencia

def doblarNumero2(nros):
  for indice in range(len(nros)): # len(nros) --> 3 --> range(3) --> 0,1,2
    nros[indice] = nros[indice] * 2 
  return nros

miNumeros = [10,20,5]
print(doblarNumero2(miNumeros)) # [20, 40, 10]
print(miNumeros) # 3 --> [20, 40, 10] --> Se modifico!



