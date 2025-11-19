# Introducir datos
precio_original = float(input("Introduce el precio original: "))
precio_venta = float(input("Introduce el precio de venta real: "))

# Calculos
descuento = precio_original - precio_venta
porcentaje = (descuento / precio_original) * 100

# Mostrar datos
print(f"El descuento realizado es del {porcentaje:.2f}%")
