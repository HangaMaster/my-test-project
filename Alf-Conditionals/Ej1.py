try:
    edad = int(input("Escriba su edad: "))
    if edad < 0:
        print("Edad no válida.")
    elif edad < 18:
        print("Usted es menor de edad.")
    else:
        print("Usted es mayor de edad.")
except ValueError as e:
    print("Valor no válido.")
finally:
    print("Proceso finalizado.")
