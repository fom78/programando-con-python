
paises = open("BDpaises.txt","r")


# "Argentina 33900 95 25.6 3408\n" 
# ["Argentina",33900, 95, 25.6, 3408] -- pais
filtro = input("Pais ? ")
for p in paises:
  pais= p.replace("\n","") #"Argentina,33900,95,25.6,3408"
  pais = pais.split(",")  # ["Argentina","33900", "95", "25.6", "3408"]

  pais[1] = int(pais[1])
  pais[2] = int(pais[2])
  pais[3] = float(pais[3])
  pais[4] = int(pais[4]) # ["Argentina",33900, 95, 25.6, 3408]

  if filtro.lower() in pais[0].lower():
    print(f"{pais[0]:20} tiene {pais[1]*1000:15,} habitantes")

print("FIN")
paises.close()

