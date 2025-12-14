duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana (ej: domingo, lunes): ").lower()
turno = input("Introduce el turno (mañana/tarde): ").lower()

costo_base = 0

if duracion <= 5:
    costo_base = 1.00
elif duracion <= 8:
    costo_base = 1.00 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo_base = 1.00 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo_base = 1.00 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

impuesto = 0
if dia == "domingo":
    impuesto = costo_base * 0.03
elif turno == "mañana":
    impuesto = costo_base * 0.15
elif turno == "tarde":
    impuesto = costo_base * 0.10

total = costo_base + impuesto

print(f"El costo de la llamada es: {costo_base:.2f} euros")
print(f"El impuesto a pagar es: {impuesto:.2f} euros")
print(f"El total a pagar es: {total:.2f} euros")
