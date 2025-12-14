numero = int(input("Introduce el número del dado (1-6): "))

if numero < 1 or numero > 6:
    print("ERROR: número incorrecto.")
else:
    opuesto = ""
    if numero == 1:
        opuesto = "seis"
    elif numero == 2:
        opuesto = "cinco"
    elif numero == 3:
        opuesto = "cuatro"
    elif numero == 4:
        opuesto = "tres"
    elif numero == 5:
        opuesto = "dos"
    elif numero == 6:
        opuesto = "uno"

    print(f"En la cara opuesta está el {opuesto}.")
