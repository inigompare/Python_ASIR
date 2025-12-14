dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

es_correcta = False

if mes >= 1 and mes <= 12:
    if mes == 2:
        # Comprobar bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia >= 1 and dia <= 29:
                es_correcta = True
        else:
            if dia >= 1 and dia <= 28:
                es_correcta = True
    elif mes in [4, 6, 9, 11]:
        if dia >= 1 and dia <= 30:
            es_correcta = True
    else:  # 1, 3, 5, 7, 8, 10, 12
        if dia >= 1 and dia <= 31:
            es_correcta = True

if es_correcta:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
