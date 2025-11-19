# Introducir datos
n1 = float(input("Introducir primer número: "))
n2 = float(input("Introducir segundo número: "))

# Calculos y muestra de datos
print(f"Suma: {n1 + n2}")
print(f"Resta: {n1 - n2}")
print(f"Producto: {n1 * n2}")
if n2 == 0:
    print("División: No se puede dividir por cero.")
else:
    print(f"Division: {n1 / n2: .2f}")
