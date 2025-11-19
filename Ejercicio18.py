# Entrada de datos
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El mayor es: {num1}")
elif num2 > num1:  # 'elif' significa 'si no, comprueba esto...'
    print(f"El mayor es: {num2}")
else:
    print("Los dos números son iguales.")
