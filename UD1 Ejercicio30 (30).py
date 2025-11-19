# Mostrar datos e introducir
print("Piensa un número del 1 al 100.")
print("Respóndeme 'mayor', 'menor' o 'igual'.")

limite_inferior = 1
limite_superior = 100

while True:
    # El ordenador hace su suposición (la mitad del rango)
    # Usamos '//' (división entera)
    intento = (limite_inferior + limite_superior) // 2

    # .lower() convierte la respuesta a minúsculas
    respuesta = input(f"¿Tu número es {intento}?: ").lower()

    if respuesta == "igual":
        print("¡Genial! He adivinado.")
        break
    elif respuesta == "mayor":
        # Tu número es MAYOR que mi intento.
        # Descarto la mitad inferior.
        limite_inferior = intento + 1
    elif respuesta == "menor":
        # Tu número es MENOR que mi intento.
        # Descarto la mitad superior.
        limite_superior = intento - 1
    else:
        print("Por favor, responde 'mayor', 'menor' o 'igual'.")
