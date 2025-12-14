base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    potencia = base ** exponente
    print(f"El resultado de la potencia es: {potencia}")
elif exponente == 0:
    print("El resultado de la potencia es: 1")
else:  # exponente < 0
    potencia = 1 / (base ** abs(exponente))
    print(f"El resultado de la potencia es: {potencia}")
