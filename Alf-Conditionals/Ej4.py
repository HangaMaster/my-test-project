try:
    a = int(input("Introduzca un número entero: "))
    if a % 2 == 0:
        print("Número par.")
    else:
        print("Número impar.")
except ValueError:
    print("Número no válido.")
