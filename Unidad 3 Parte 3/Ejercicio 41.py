cantidad = int(input("Introduce la cantidad de números a introducir: "))

mayores = 0
menores = 0
iguales = 0

for i in range(cantidad):
    num = float(input(f"Introduce el número {i+1}: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print(f"Números mayores que 0: {mayores}")
print(f"Números menores que 0: {menores}")
print(f"Números iguales a 0: {iguales}")
