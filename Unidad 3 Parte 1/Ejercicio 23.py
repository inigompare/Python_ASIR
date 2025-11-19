# Introducir datos
valor_compra = float(input("Introduce el valor de compra: "))
forma_pago = input("Forma de pago ('contado' o 'tarjeta'): ").lower()

# Descuentos y recargos
descuento = 0
recargo = 0
total_a_pagar = valor_compra

# Evaluar forma de pago
if forma_pago == "contado":
    # 5% de descuento [cite: 125]
    descuento = valor_compra * 0.05
    total_a_pagar = valor_compra - descuento
    print(f"¡Pago al contado! Descuento aplicado: {descuento:.2f}")

# Pago con tarjeta
elif forma_pago == "tarjeta":
    # 3% de recargo [cite: 126]
    recargo = valor_compra * 0.03
    total_a_pagar = valor_compra + recargo
    print(f"Pago con tarjeta. Recargo aplicado: {recargo:.2f}")

# Forma de pago no reconocida
else:
    print("Forma de pago no reconocida. No se aplicó descuento/recargo.")

# Mostrar total a pagar
print(f"Total a pagar: {total_a_pagar:.2f}")
