print("Piensa un número del 1 al 100 y yo lo adivinaré.")
input("Pulsa Enter cuando estés listo...")

bajo = 1
alto = 100
intentos = 0

while True:
    intento = (bajo + alto) // 2
    intentos += 1
    print(f"¿Es {intento} tu número?")
    respuesta = input("Responde 'mayor', 'menor' o 'igual': ").strip().lower()
    if respuesta == "igual":
        print(f"¡He adivinado tu número en {intentos} intentos!")
        break
    elif respuesta == "mayor":
        bajo = intento + 1
    elif respuesta == "menor":
        alto = intento - 1
    else:
        print("Respuesta no válida. Escribe 'mayor', 'menor' o 'igual'.")
