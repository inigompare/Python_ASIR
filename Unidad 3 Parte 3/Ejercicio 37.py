peso = float(input("Introduce el peso del paquete (kg): "))
zona = int(input("Introduce la zona de destino (1-5): "))

costo = 0

# NOTA: La tabla de costos y zonas no aparecía en la imagen proporcionada.
# Aquí va la estructura donde se deberían añadir los precios.

if zona == 1:  # América del Norte
    costo = peso * 24.00  # Precio de ejemplo
elif zona == 2:  # América Central
    costo = peso * 20.00  # Precio de ejemplo
elif zona == 3:  # América del Sur
    costo = peso * 21.00  # Precio de ejemplo
elif zona == 4:  # Europa
    costo = peso * 10.00  # Precio de ejemplo
elif zona == 5:  # Asia
    costo = peso * 18.00  # Precio de ejemplo
else:
    print("Zona incorrecta")

if costo > 0:
    print(f"El costo de envío es: {costo:.2f} euros")
