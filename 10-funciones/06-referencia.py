

def transformarHeroe(data, modo=2):
  if modo == 1:
    print("Mayusculas")
    for codigo in data.keys():
      data[codigo] = data[codigo].upper()
  elif modo == 2:
    print("minusculas")
    for codigo in data.keys():
      data[codigo] = data[codigo].lower()
  elif modo == 3:
    print("title")
    for codigo in data.keys():
      data[codigo] = data[codigo].title()




heroes = {
  100:"capitan america",
  120:"iron man",
  345: "hulk",
  23:"capitana marvel"
}
print("Original-->>",heroes)

# modo 1 mayusculas, modo 2 minusculas, modo 3 title



transformarHeroe(heroes, modo=3)

print(heroes)
