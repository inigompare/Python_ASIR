# Sumas
suma_total = 0
producto_total = 1  # ¡Importante! Empezar en 1

# Bucle for que va del 1 al 10
for i in range(1, 11):
    suma_total = suma_total + i
    producto_total = producto_total * i

print(f"La suma de los 10 primeros números es: {suma_total}")
print(f"El producto de los 10 primeros números es: {producto_total}")
