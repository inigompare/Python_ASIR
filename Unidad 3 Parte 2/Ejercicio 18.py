# Versión sencilla: calcula A^B sin usar **
a = float(input("Introduce A (base): "))
b = int(input("Introduce B (exponente entero): "))

# Manejo de caso especial
if a == 0 and b < 0:
    print("Error: 0 no puede elevarse a exponente negativo.")
else:  # Cálculo de la potencia
    resultado = 1.0
    for _ in range(abs(b)):
        resultado *= a
    if b < 0:
        resultado = 1.0 / resultado
    print(f"{a} ^ {b} = {resultado}")
