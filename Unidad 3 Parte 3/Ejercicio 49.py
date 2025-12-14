total_horas = 0

for dia in range(1, 7):
    horas = float(input(f"Introduce las horas trabajadas el día {dia}: "))
    total_horas += horas

pago_hora = float(input("Introduce el precio por hora: "))
sueldo = total_horas * pago_hora

print(f"El total de horas trabajadas es: {total_horas}")
print(f"El sueldo a recibir es: {sueldo:.2f} euros")
