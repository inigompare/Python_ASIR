
HH = int(input("Hora de salida: "))
MM = int(input("Minutos de salida: "))
SS = int(input("Segundos de salida: "))
T = int(input("Tiempo de viaje en segundos: "))

total_segundos_inicial = HH * 3600 + MM * 60 + SS
total_segundos_final = total_segundos_inicial + T

HH_llegada = (total_segundos_final // 3600) % 24
MM_llegada = (total_segundos_final % 3600) // 60
SS_llegada = (total_segundos_final % 3600) % 60

print(
    f"La hora de llegada a la ciudad B es: {HH_llegada}:{MM_llegada}:{SS_llegada}")
