num_alumnos = int(input("Introduce el número de alumnos: "))

costo_alumno = 0
costo_total = 0

if num_alumnos >= 100:
    costo_alumno = 65
    costo_total = num_alumnos * costo_alumno
elif num_alumnos >= 50:
    costo_alumno = 70
    costo_total = num_alumnos * costo_alumno
elif num_alumnos >= 30:
    costo_alumno = 95
    costo_total = num_alumnos * costo_alumno
else:
    costo_alumno = 4000 / num_alumnos
    costo_total = 4000

print(f"El costo por alumno es: {costo_alumno:.2f} euros")
print(f"El pago a la compañía de autobuses es: {costo_total:.2f} euros")
