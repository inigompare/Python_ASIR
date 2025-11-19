# Introducir la altura de la escalera
altura = int(input("Introduce la altura de la escalera: "))

# Construir la escalera con números
n = 1
for i in range(1, altura + 1):
    print(f"{n}" * i)
    n = n + 1
