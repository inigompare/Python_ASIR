# Mostrar datos e introducir
hubo_un_diez = False  # La bandera empieza "bajada"

print("Introduce notas (0-10), (-1 para terminar):")

while True:
    nota = float(input("Nota: "))

    if nota == -1:
        break  # Salir del bucle

    if nota == 10:
        hubo_un_diez = True  # "Levantamos" la bandera

# Al final, miramos la bandera
if hubo_un_diez:
    print("Sí, se introdujo al menos un 10.")
else:
    print("No se introdujo ningún 10.")
