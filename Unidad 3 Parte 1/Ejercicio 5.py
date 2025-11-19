# Importamos la modulo math
import math
# Variables
radio = float(input("Introduce el radio: "))
diametro = radio * 2
# Calculos con variables y modulo math
circunferencia = math.pi * diametro
area = math.pi * (radio ** 2)
volumen = (4/3) * math.pi * (radio ** 3)
# Mostramos datos
print(f"Longitud circunferencia: {circunferencia:.2f}")
print(f"Área del círculo: {area:.2f}")
print(f"Volumen esfera: {volumen:.2f}")
