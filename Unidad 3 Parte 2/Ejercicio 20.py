# Programa que desglosa una cantidad (múltiplo de 5) en el mínimo número de billetes.

try:
    cantidad = int(input("Introduce una cantidad de euros (múltiplo de 5): "))

    if cantidad % 5 != 0:
        print("Error: La cantidad debe ser múltiplo de 5.")
    else:
        print(f"Desglose de {cantidad} €:")

        # Lista de billetes disponibles ordenados de mayor a menor
        billetes = [500, 200, 100, 50, 20, 10, 5]

        for billete in billetes:
            # Calculamos cuántos billetes de este tipo caben
            num_billetes = cantidad // billete

            # Si cabe alguno, lo mostramos y actualizamos la cantidad restante
            if num_billetes > 0:
                # Usamos singular o plural según corresponda para que quede mejor (opcional, pero elegante)
                tipo = "billete" if num_billetes == 1 else "billetes"
                print(f"{num_billetes} {tipo} de {billete} €")

                # Actualizamos la cantidad con el resto de la división
                cantidad %= billete

except ValueError:
    print("Por favor, introduce un número entero válido.")
