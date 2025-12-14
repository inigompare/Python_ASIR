numero = int(input("Introduce un número para calcular su factorial: "))

if numero < 0:
    print("No existe el factorial de un número negativo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i

    print(f"{numero}! = {factorial}")
