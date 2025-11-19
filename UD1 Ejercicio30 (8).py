# PASO 1: DEFINIR CONSTANTES
METROS_POR_MILLA = 1852

# PASO 2: ENTRADA DE DATOS
millas_marinas = float(input("Introduce la distancia en millas marinas: "))

# PASO 3: CÁLCULO (PROCESAMIENTO)
metros = millas_marinas * METROS_POR_MILLA

# PASO 4: SALIDA DE DATOS
print(f"{millas_marinas} millas marinas equivalen a {metros} metros.")
