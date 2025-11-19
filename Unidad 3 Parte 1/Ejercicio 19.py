# Variable saldo
saldo = 1000  # Saldo inicial

# Bucle infinito y Menú
while True:
    print("\n--- BIENVENIDO A SU CAJERO VIRTUAL ---")
    print(f"Saldo actual: ${saldo}")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

# Condicionales
    if opcion == "1":
        dolares = float(input("¿Cuánto dinero desea ingresar?: "))
        if dolares > 0:
            saldo += dolares
            print(f"Ingreso exitoso. Nuevo saldo: ${saldo}")
        else:
            print("La cantidad debe ser positiva.")

    elif opcion == "2":
        dolares = float(input("¿Cuánto dinero desea retirar?: "))
        if dolares > saldo:
            print("Error: Fondos insuficientes.")
        elif dolares > 0:
            saldo -= dolares
            print(f"Retirada exitosa. Nuevo saldo: ${saldo}")
        else:
            print("La cantidad debe ser positiva.")

    elif opcion == "3":
        print("Gracias por usar nuestro cajero. ¡Hasta luego!")
        break  # Rompe el bucle y termina el programa

    else:
        print("Opción no válida. Intente de nuevo.")
