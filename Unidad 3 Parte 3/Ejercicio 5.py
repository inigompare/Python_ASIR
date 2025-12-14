# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
# Fórmula: (F - 32) * 5/9

fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius")
