dia = int(input("Introduce el número del día de la semana (1-7): "))

dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

if dia in dias_semana:
    print(f"El día correspondiente es: {dias_semana[dia]}")
else:
    print("ERROR: número incorrecto.")
