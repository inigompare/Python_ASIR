# Pedimos tres números
n1 = float(input("Número 1º: "))
n2 = float(input("Número 2º: "))
n3 = float(input("Número 3º: "))

# Determinar el mayor
mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3

# Determinar el menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Mostrar datos
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")

if n1 == n2 == n3:
    print("Los tres números son iguales.")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("Hay dos números iguales.")
else:
    print("No hay números iguales.")
