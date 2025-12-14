# Ejercicio 10
# Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales.

suma = 0
producto = 1

# Los 10 primeros números naturales son 1, 2, ..., 10
for i in range(1, 11):
    suma += i
    producto *= i

print(f"Los 10 primeros números naturales son: {list(range(1, 11))}")
print(f"Suma: {suma}")
print(f"Producto: {producto}")
