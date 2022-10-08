precio = float(input("precio de la prenda: "))
plan1 = precio * 0.85
plan2 = precio * 0.95
plan3 = precio / 3
plan4 = (precio * 1.20)/12
print("los planes de pago son: ")
print(f"{'Plan1 efectivo 15% de descuento ':50}$ {plan1:.2f}")
print(f"{'plan2 plataforma digital 5% de descuento ':50}$ {plan2:.2f}")
print(f"{'plan3 tres cuotas sin interes de: ':50}$ {plan3:.2f}")
print(f"{'plan4 20% de interes en 12 cuotas de: ':50}$ {plan4:.2f}")