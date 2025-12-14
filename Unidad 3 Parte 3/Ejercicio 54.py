import time
import os

horas = 0
minutos = 0
segundos = 0

print("Iniciando cronómetro... (Pulsa Ctrl+C para detener)")
try:
    while True:
        # Limpiar pantalla (opcional, para que se vea como un reloj fijo)
        # os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{horas:02}:{minutos:02}:{segundos:02}")
        time.sleep(1)

        segundos += 1
        if segundos == 60:
            segundos = 0
            minutos += 1
            if minutos == 60:
                minutos = 0
                horas += 1
                if horas == 24:
                    horas = 0
except KeyboardInterrupt:
    print("\nCronómetro detenido.")
