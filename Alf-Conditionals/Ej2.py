pw = input("Escriba su contraseña: ")
conf = input("Confirme la contraseña: ")
if pw.upper() == conf.upper():
    print("OK")
else:
    print("Las contraseñas no coinciden.")
