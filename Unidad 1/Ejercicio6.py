# ENTRADA DE DATOS
precio_original = float(input("Introduce el precio original del artículo: "))
precio_venta = float(input("Introduce el precio de venta real: "))

# CÁLCULOS
descuento_en_dinero = precio_original - precio_venta
porcentaje_descuento = (descuento_en_dinero / precio_original) * 100

# SALIDA DE DATOS
print(f"El descuento aplicado ha sido del {porcentaje_descuento:.2f}%")
