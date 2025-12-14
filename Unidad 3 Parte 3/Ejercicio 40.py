suma = 0
cantidad = 0
numero = float(input("Introduce un número (0 para terminar): "))

while numero != 0:
    suma += numero
    cantidad += 1
    numero = float(input("Introduce otro número (0 para terminar): "))

if cantidad > 0:
    media = suma / cantidad
    print(f"La suma es: {suma}")
    print(f"La media es: {media}")
else:
    print("No se han introducido números.")
