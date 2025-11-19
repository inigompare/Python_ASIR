# Introducir datos
nota = float(input("Introduce la calificación numérica (0-10): "))

# Condicionales
if 0 <= nota < 3:
    calificacion = "Muy Deficiente"  # De 0 a <3
elif 3 <= nota < 5:
    calificacion = "Insuficiente"  # De 3 a <5
elif 5 <= nota < 6:
    calificacion = "Suficiente"  # De 5 a <6
elif 6 <= nota < 7:
    calificacion = "Bien"  # De 6 a <7
elif 7 <= nota < 9:
    calificacion = "Notable"  # De 7 a <9
elif 9 <= nota <= 10:
    calificacion = "Sobresaliente"  # De 9 a 10
else:
    calificacion = "ERROR: Nota fuera de rango (debe ser de 0 a 10)."

print(f"La calificación numérica {nota} equivale a: {calificacion}")
