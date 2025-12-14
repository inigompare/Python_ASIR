num1 = float(input("Introduce el dividendo: "))
num2 = float(input("Introduce el divisor: "))

if num2 != 0:
    division = num1 / num2
    print(f"El resultado de la división es: {division}")
else:
    print("Aviso: No se puede dividir por cero")
