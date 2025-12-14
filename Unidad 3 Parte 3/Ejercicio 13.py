import math

numero = float(input("Introduce un número: "))

raiz_cuadrada = math.sqrt(numero)
raiz_cubica = numero ** (1/3)

print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica:.2f}")
