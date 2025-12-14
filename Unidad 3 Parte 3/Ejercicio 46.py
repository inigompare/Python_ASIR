base = float(input("Introduce la base (real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

while exponente < 0:
    print("El exponente debe ser positivo.")
    exponente = int(input("Introduce el exponente (entero positivo): "))

potencia = 1

for i in range(exponente):
    potencia = potencia * base

print(f"El resultado de la potencia es: {potencia}")
