# Introducir datos
cantidad = int(input("Introduce una cantidad (múltiplo de 5): "))

# Lista de billetes, de mayor a menor
billetes = [500, 200, 100, 50, 20, 10, 5]

print(f"Para {cantidad} €, necesitas:")

# Recorremos la lista de billetes
for billete in billetes:
    # 1. ¿Cuántos billetes de este tipo caben?
    num_billetes = cantidad // billete

    # 2. Si caben (es > 0), los mostramos
    if num_billetes > 0:
        print(f"- {num_billetes} billete(s) de {billete} €")

    # 3. ¿Cuánto dinero "sobra" para el siguiente billete?
    cantidad = cantidad % billete
