# Introducir números
nota = float(input("Introduce la calificación (0-10): "))

# Condicionales
if nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10.")
elif nota < 3:  # Si llega aquí, ya sabemos que es >= 0
    print("Muy Deficiente.")
elif nota < 5:  # Si llega aquí, ya sabemos que es >= 3
    print("Insuficiente.")
elif nota < 6:  # Si llega aquí, ya sabemos que es >= 5
    print("Suficiente.")
elif nota < 7:  # Si llega aquí, ya sabemos que es >= 6
    print("Bien.")
elif nota < 9:  # Si llega aquí, ya sabemos que es >= 7
    print("Notable.")
else:  # Si llega aquí, es que es >= 9 (y <= 10)
    print("Sobresaliente.")
