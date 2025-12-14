opcion = ""

while opcion != "3":
    print("\n--- MENÚ ---")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Has elegido la opción 1.")
    elif opcion == "2":
        print("Has elegido la opción 2.")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción incorrecta. Inténtalo de nuevo.")
