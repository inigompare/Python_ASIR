# Esta es nuestra "bandera". Empieza en Falso.
ha_leido_negativo = False

print("Introduce 100 números (no nulos):")
# Este bucle se repetirá 100 veces
for i in range(100):
    num = float(input(f"Número {i + 1}/100: "))

    if num < 0:
        # Si encontramos un negativo, "levantamos la bandera"
        ha_leido_negativo = True

# Al final del bucle, miramos la bandera
if ha_leido_negativo:
    print("\nSí, se han leído números negativos.")
else:
    print("\nNo se han leído números negativos.")
