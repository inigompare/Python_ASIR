
distancia = float(input("Introduce la distancia entre los vehículos (km): "))
v1 = float(input("Introduce la velocidad del vehículo más lento (v1) km/h: "))
v2 = float(input("Introduce la velocidad del vehículo más rápido (v2) km/h: "))

# Tiempo en horas = distancia / velocidad_relativa
velocidad_relativa = v2 - v1
tiempo_horas = distancia / velocidad_relativa
tiempo_minutos = tiempo_horas * 60

print(
    f"El vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos.")
