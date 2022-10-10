print("listas y tuplas")

cadena = "Hola"

# vocales= ["a","e","i","o","u"]

# miTupla = (2,4,5,6, "r",True, ["a","b"],(3,6))

# print(miTupla)

# print(vocales)

# vocales[3] = 234.78
# print(miTupla[4])
# # miTupla[4] = 34
# print(vocales)

# print(len(miTupla), len(vocales))

# print(type(vocales[3:4]))
# print(type(vocales[3]))

vocales= list("aeiou")
# vocales.append(34)
# vocales.append("Casa")

vocales.extend(["x","y","z"])

vocales.remove("w")
print(vocales)