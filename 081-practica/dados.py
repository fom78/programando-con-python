from random import randint
ronda=1
dados=[] # [2,4,5,5,1]
puntaje = 0
puntajeTotal = 0
while ronda <= 5:
  print(f".:: Ronda #{ronda}")
  tirarDados = input("Tirar dados? (s/n): ")
  if tirarDados == "n":
    print("Daleeee... tira los dados ...")
    continue

  # Carga de los dados o la tirada de dados sobre la mesa
  for i in range(5): # 0, 1, 2, 3, 4
    dados.append(randint(1,6))

  print("Tus dados >>> ", dados)
  trio = 0
  par1 = 0
  par2 = 0
  puntaje=0
 
  for dado in dados:
    if dados.count(dado) == 5: #[3,3,3,3,3]
      print(f"Felicitaciones Todos iguales ({dado}) +20")
      puntaje = puntaje + 20
      break
    elif dados.count(dado) == 4: #[3,3,3,6,3]
      print(f"Felicitaciones 4 dados iguales ({dado}) +12")
      puntaje = puntaje + 12
      break
    elif dados.count(dado) == 3: #[3,3,6,6,3]
      if trio == 0:
        print(f"Sacaste un trio: {dado}")
        trio = dado
    elif dados.count(dado) == 2: #[3,2,5,6,3]
      if par1 == 0:
        print(f"Sacaste un par: {dado}")
        par1 = dado
      elif par1 != dado and par2 == 0:
        print(f"Sacaste un par: {dado}")
        par2 = dado
    
  if par1 != 0 and par2 != 0:
    print(">>>> Doble Par +5")
    puntaje = puntaje + 5
  elif par1 != 0 or par2 != 0:
    if trio != 0:
      print(">>>> Full +9")
      puntaje = puntaje + 9
    else:
      print(">>>> Par Simple +2")
      puntaje = puntaje + 2
  else:
    if trio != 0:
      print(f">>>> Trio de {trio} +6")
      puntaje = puntaje + 6

  print(f"Puntaje de la ronda: {puntaje}")

  ronda = ronda + 1
  puntajeTotal = puntajeTotal + puntaje
  
  dados.clear()

print(f"Puntaje total: {puntajeTotal}")

