
sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el importe de la primera venta: "))
venta2 = float(input("Introduce el importe de la segunda venta: "))
venta3 = float(input("Introduce el importe de la tercera venta: "))

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.10
sueldo_total = sueldo_base + comision

print(f"La comisión total es de: {comision:.2f}")
print(f"El sueldo total a recibir es: {sueldo_total:.2f}")
