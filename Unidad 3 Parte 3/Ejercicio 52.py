num_trabajadores = int(input("Introduce el número de trabajadores: "))
tarifa_hora = float(input("Introduce la tarifa por hora: "))

total_pagado = 0

for i in range(1, num_trabajadores + 1):
    horas = float(
        input(f"Introduce las horas trabajadas por el trabajador {i}: "))
    sueldo = horas * tarifa_hora
    print(f"El sueldo del trabajador {i} es: {sueldo:.2f} euros")
    total_pagado += sueldo

print(f"El total pagado por la empresa es: {total_pagado:.2f} euros")
