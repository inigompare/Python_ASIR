limite_inferior = int(input("Introduce el límite inferior: "))
limite_superior = int(input("Introduce el límite superior: "))

while limite_inferior > limite_superior:
    print("El límite inferior debe ser menor o igual que el superior.")
    limite_inferior = int(input("Introduce el límite inferior: "))
    limite_superior = int(input("Introduce el límite superior: "))

suma_dentro = 0
fuera_intervalo = 0
igual_limites = False

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    if numero > limite_inferior and numero < limite_superior:
        suma_dentro += numero
    elif numero < limite_inferior or numero > limite_superior:
        fuera_intervalo += 1
    else:
        igual_limites = True

    numero = int(input("Introduce otro número (0 para terminar): "))

print(f"La suma de los números dentro del intervalo es: {suma_dentro}")
print(f"Números fuera del intervalo: {fuera_intervalo}")

if igual_limites:
    print("Se ha introducido algún número igual a los límites.")
else:
    print("No se ha introducido ningún número igual a los límites.")
