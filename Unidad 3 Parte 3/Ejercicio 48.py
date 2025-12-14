ahorro_total = 0

for mes in range(1, 13):
    deposito = float(
        input(f"Introduce la cantidad a depositar en el mes {mes}: "))
    ahorro_total += deposito
    print(f"Dinero ahorrado hasta el mes {mes}: {ahorro_total:.2f} euros")

print(f"El ahorro total al final del año es: {ahorro_total:.2f} euros")
