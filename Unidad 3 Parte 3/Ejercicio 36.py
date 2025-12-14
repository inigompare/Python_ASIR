mes = int(input("Introduce el número del mes (1-12): "))

if mes < 1 or mes > 12:
    print("ERROR: mes incorrecto.")
else:
    if mes == 2:
        print("El mes tiene 28 días (o 29 si es bisiesto)")
    elif mes in [4, 6, 9, 11]:
        print("El mes tiene 30 días")
    else:
        print("El mes tiene 31 días")
