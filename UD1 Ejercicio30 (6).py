# PASO 1: IMPORTAR HERRAMIENTAS
import math

# PASO 2: ENTRADA DE DATOS
radio = float(input("Introduce el radio: "))

# PASO 3: DEFINIR CONSTANTES Y VARIABLES INICIALES
pi = math.pi
diametro = 2 * radio

#  PASO 4: CÁLCULOS (PROCESAMIENTO)
longitud_circunferencia = pi * diametro
area_circulo = pi * (radio ** 2)
volumen_esfera = (4/3) * pi * (radio ** 3)

#  PASO 5: SALIDA DE DATOS
print(f"--- Resultados para un radio de {radio} ---")
print(f"Longitud de la circunferencia: {longitud_circunferencia}")
print(f"Área del círculo: {area_circulo}")
print(f"Volumen de la esfera: {volumen_esfera}")
