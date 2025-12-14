# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

minutos_totales = int(input("Introduce la cantidad de minutos: "))

horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60

print(f"{minutos_totales} minutos son {horas} horas y {minutos_restantes} minutos.")
