# Introducir numero
num = int(input("Introduce un número (0 - 99999): "))

# Mostrar datos
if 0 <= num <= 99999:
    cifras = len(str(num))
    print(f"El número {num} tiene {cifras} cifras.")
else:
    print("Error: El número está fuera del rango solicitado.")
