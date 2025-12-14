caracter = input("Introduce un carácter (espacio para terminar): ")

while caracter != " ":
    if caracter.lower() in "aeiouáéíóúü":
        print("VOCAL")
    else:
        print("NO VOCAL")

    caracter = input("Introduce un carácter (espacio para terminar): ")
