a = int(input("Introduzca el dividendo: "))
b = int(input("Introduzca el divisor: "))
try:
    print(a / b)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
