# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math

cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"La hipotenusa del triángulo es: {hipotenusa}")
