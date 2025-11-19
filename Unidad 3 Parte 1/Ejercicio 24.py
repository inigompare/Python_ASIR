# Introducir datos
compra = float(input("Introduce el precio de compra: "))
dia_semana = input(
    "Introduce el día de la semana: ").lower()

descuento = 0
total_a_pagar = compra

# Comprobamos la condición compuesta
if dia_semana == "martes" or dia_semana == "jueves":
    descuento_porcentaje = 0.15
    descuento = compra * descuento_porcentaje
    total_a_pagar = compra - descuento
    print(
        f"¡Hoy es {dia_semana.capitalize()}! Descuento aplicado (15%): {descuento:.2f}")
else:
    print(f"Hoy es {dia_semana.capitalize()}. No hay descuento.")

print(f"Total a pagar: {total_a_pagar:.2f}")
