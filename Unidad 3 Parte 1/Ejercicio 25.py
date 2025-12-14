# Intro ducir datos
print("--- SISTEMA DE MATRÍCULA ---")
nombre = input("Ingrese nombre del postulante: ")

print("\nFacultades disponibles:")
print("1. Ingeniería de Sistemas")
print("2. Derecho")
print("3. Ingeniería Naviera")
print("4. Ingeniería Pesquera")
print("5. Contabilidad")
print("6. Administración")

# Pedimos la opción como número entero
opcion = int(input("Seleccione la facultad (1-6): "))

# Variables iniciales
facultad = ""
matricula = 0
mensualidad = 0

# ESTRUCTURA SWITCH (match) CON DATOS REALES
match opcion:
    case 1:
        facultad = "Ing. de Sistemas"
        matricula = 350.00
        mensualidad = 650.00
    case 2:
        facultad = "Derecho"
        matricula = 300.00
        mensualidad = 550.00
    case 3:
        facultad = "Ing. Naviera"
        matricula = 300.00
        mensualidad = 500.00
    case 4:
        facultad = "Ing. Pesquera"
        matricula = 310.00
        mensualidad = 460.00
    case 5:
        facultad = "Contabilidad"
        matricula = 280.00
        mensualidad = 490.00
    case 6:
        facultad = "Administración"
        matricula = 360.00
        mensualidad = 520.00
    case _:
        print("Opción no válida.")
        facultad = "Error"

# CÁLCULOS (Solo si la facultad es válida)
if facultad != "Error":
    # 1. Sumamos matrícula y mensualidad
    importe_base = matricula + mensualidad

    # 2. Calculamos el IGV (18% de esa suma)
    igv = importe_base * 0.18

    # 3. Monto final
    monto_final = importe_base + igv

    #  SALIDA DE DATOS
    print(f"\n--- BOLETA DE VENTA: {nombre.upper()} ---")
    print(f"Facultad:            {facultad}")
    print(f"Importe Matrícula:   S/ {matricula:.2f}")
    print(f"Mensualidad:         S/ {mensualidad:.2f}")
    print("-----------------------------------")
    print(f"Subtotal:            S/ {importe_base:.2f}")
    print(f"IGV (18%):           S/ {igv:.2f}")
    print("-----------------------------------")
    print(f"MONTO FINAL A PAGAR: S/ {monto_final:.2f}")
