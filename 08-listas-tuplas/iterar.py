

colores=[(12,"rojo"),(23,"verde"),(34,"azul")]

colores.append((100,"negro"))
colores.extend([(2,"rosa"),(23,"violeta")])
for color in colores:
  if "o" in color[1]:
    print(color)

print("Fin")