
total_compra = float(input("Introduce el total de la compra: "))

descuento = total_compra * 0.15
total_pagar = total_compra - descuento

print(f"El descuento aplicado es de: {descuento:.2f}")
print(f"El total a pagar es de: {total_pagar:.2f}")
