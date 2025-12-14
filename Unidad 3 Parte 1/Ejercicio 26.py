import random

# Lanzar dados
print("--- CASINO: LANZAMIENTO DE DADOS ---")
input("Presiona Enter para lanzar los dados...")

# 1. Simulamos el lanzamiento (números aleatorios del 1 al 6)
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print(f"\nResultados: [{dado1}] [{dado2}] [{dado3}]")

# 2. Contamos cuántos seises han salido (Lógica previa al switch)
cantidad_seises = 0

if dado1 == 6:
    cantidad_seises += 1
if dado2 == 6:
    cantidad_seises += 1
if dado3 == 6:
    cantidad_seises += 1

# 3. Usamos el SWITCH (match) sobre la cantidad contada
print("\n--- Veredicto ---")
match cantidad_seises:
    case 3:
        print("¡Excelente!")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")
    case _:
        print("Error en el conteo")
