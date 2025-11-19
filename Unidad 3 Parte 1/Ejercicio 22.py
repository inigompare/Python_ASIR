anos = float(input("Introduce la cantidad de años: "))

# Constantes de conversión
DIAS_POR_ANO = 365
HORAS_POR_DIA = 24
MINUTOS_POR_HORA = 60
SEGUNDOS_POR_MINUTO = 60

# Cálculos
dias = anos * DIAS_POR_ANO
horas = dias * HORAS_POR_DIA
minutos = horas * MINUTOS_POR_HORA
segundos = minutos * SEGUNDOS_POR_MINUTO

# Salida de resultados
print(f"\n--- Conversión para {anos:.2f} años ---")
print(f"Equivalen a {dias:.2f} días.")
print(f"Equivalen a {horas:.2f} horas.")
print(f"Equivalen a {minutos:.2f} minutos.")
print(f"Equivalen a {segundos:.2f} segundos.")
