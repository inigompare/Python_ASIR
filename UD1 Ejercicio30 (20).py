# Introducir datos
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))

# Primero, el caso más específico:
if n1 == n2 and n2 == n3:
    print("Los tres números son iguales.")
else:
    # Si no son todos iguales, buscamos el max y min
    # Ponemos los números en una lista
    numeros = [n1, n2, n3]

    # max() y min() son funciones de Python
    print(f"El número mayor es: {max(numeros)}")
    print(f"El número menor es: {min(numeros)}")

    # Comprobamos si hay igualdades parciales
    if n1 == n2:
        print("El primero y el segundo son iguales.")
    elif n2 == n3:
        print("El segundo y el tercero son iguales.")
    elif n1 == n3:
        print("El primero y el tercero son iguales.")
