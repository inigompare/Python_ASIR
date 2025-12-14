import random

numero_secreto = random.randint(1, 100)
intentos = 10
acertado = False

print("He pensado un número del 1 al 100. ¡Intenta adivinarlo!")

while intentos > 0 and not acertado:
    print(f"Te quedan {intentos} intentos.")
    numero = int(input("Introduce un número: "))

    if numero == numero_secreto:
        acertado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

    if not acertado:
        intentos -= 1

if acertado:
    print(f"¡Has acertado! El número era {numero_secreto}.")
    # Corrigiendo logica de conteo
    print(
        f"Lo has conseguido en {10 - intentos + 1} intentos (si fue a la primera, 1 intento).")
else:
    print(f"Se acabaron los intentos. El número era {numero_secreto}.")
