# Verificar si se ingresó al menos una nota de 10
encontro_diez = False

# Bucle para ingresar notas
while True:
    nota = float(input("Introduce una nota (0-10) o -1 para terminar: "))
    if nota == -1:
        break
    if nota == 10:
        encontro_diez = True
# Resultados
if encontro_diez:
    print("Sí hubo al menos una nota de 10.")
else:
    print("No hubo ninguna nota de 10.")
