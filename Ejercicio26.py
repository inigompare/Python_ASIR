# 1. Pedir datos
nombre = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora (€): "))

# 2. Calcular Salario Bruto
if horas <= 35:
    salario_bruto = horas * tarifa
else:
    # Horas normales + Horas extra
    horas_normales = 35
    horas_extra = horas - 35
    salario_bruto = (horas_normales * tarifa) + (horas_extra * tarifa * 1.5)

# 3. Calcular Impuestos
impuestos_totales = 0

# Lógica de tramos (se aplica de arriba a abajo)
# El salario bruto es 1000€.
# 1000 - 900 = 100€ (se tasan al 45%) -> 45€
# 400€ fijos (se tasan al 25%) -> 100€
# 500€ fijos (se tasan al 0%) -> 0€
# Total impuestos: 145€

if salario_bruto > 900:
    # Impuesto del tramo 3 (45%)
    impuestos_totales += (salario_bruto - 900) * 0.45
    # Impuesto del tramo 2 (completo)
    impuestos_totales += 400 * 0.25
elif salario_bruto > 500:
    # Impuesto solo del tramo 2 (25%)
    impuestos_totales += (salario_bruto - 500) * 0.25
# Si salario_bruto <= 500, impuestos_totales se queda en 0

salario_neto = salario_bruto - impuestos_totales

# 4. Mostrar resultados
print(f"\n--- Recibo de {nombre} ---")
print(f"Salario Bruto: {salario_bruto:.2f} €")
print(f"Tasas (Impuestos): {impuestos_totales:.2f} €")
print(f"Salario Neto: {salario_neto:.2f} €")
