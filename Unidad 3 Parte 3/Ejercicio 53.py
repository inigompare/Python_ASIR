num_trabajadores = int(input("Introduce el número de trabajadores: "))
tarifa_hora = float(input("Introduce la tarifa por hora: "))
dias_semana = int(
    input("Introduce cuántos días trabajan a la semana (ej: 5 o 6): "))

total_pagado_empresa = 0

for i in range(1, num_trabajadores + 1):
    horas_semanales = 0
    print(f"--- Trabajador {i} ---")
    for dia in range(1, dias_semana + 1):
        horas_dia = float(input(f"  Horas trabajadas el día {dia}: "))
        horas_semanales += horas_dia

    sueldo_semanal = horas_semanales * tarifa_hora
    print(
        f"  El sueldo semanal del trabajador {i} es: {sueldo_semanal:.2f} euros")
    total_pagado_empresa += sueldo_semanal

print(
    f"El total pagado por la empresa por los {num_trabajadores} empleados es: {total_pagado_empresa:.2f} euros")
