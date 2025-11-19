# Datos correctos almacenados
usuario_correcto = "admin"
password_correcto = "1234"

usuario_input = input("Usuario: ")
password_input = input("Contraseña: ")

if usuario_input == usuario_correcto and password_input == password_correcto:
    print("Inicio de sesión correcto.")
else:
    print("Nombre de usuario o contraseña incorrectos.")
