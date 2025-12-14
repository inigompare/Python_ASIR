A = float(input("Introduce el lado A: "))
B = float(input("Introduce el lado B: "))
C = float(input("Introduce el lado C: "))

# Ordenamos para Pitágoras
lados = sorted([A, B, C])

# Pitágoras: hipotenusa^2 = cateto1^2 + cateto2^2
# Usamos round para evitar problemas de precisión con float
es_rectangulo = round(lados[2]**2, 5) == round(lados[0]**2 + lados[1]**2, 5)

if es_rectangulo:
    print("El triángulo es rectángulo")
elif A == B == C:
    print("El triángulo es equilátero")
elif A == B or A == C or B == C:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
