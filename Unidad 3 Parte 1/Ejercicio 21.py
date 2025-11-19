# Introducir datos
nombre = input("Nombre del trabajador: ")
tarifa = float(input("Tarifa por hora normal: "))
horas = float(input("Horas trabajadas: "))

# Calculo de datos
MAX_NORMAL = 35  # Máximo de horas a tarifa normal
TARIFA_EXTRA = tarifa * 1.5

if horas > MAX_NORMAL:
    # Pago normal por 35h + pago extra
    bruto = (MAX_NORMAL * tarifa) + \
            ((horas - MAX_NORMAL) * TARIFA_EXTRA)
else:
    # Solo pago por horas normales
    bruto = horas * tarifa

# Calculo de impuestos
impuesto = 0
exceso1 = bruto - 500
if exceso1 > 0:
    gravar2 = min(exceso1, 400)
    impuesto += gravar2 * 0.25

    exceso2 = exceso1 - 400

    if exceso2 > 0:
        impuesto += exceso2 * 0.45

# Salario neto y resultados
neto = bruto - impuesto

print("\n" + "="*35)
print(f"TRABAJADOR: {nombre}")
print("="*35)
print(f"Salario Bruto (sin impuestos): {bruto:.2f} €")
print(f"Total Impuestos Retenidos: {impuesto:.2f} €")
print("-" * 35)
print(f"SALARIO NETO FINAL: {neto:.2f} €")
print("="*35)
