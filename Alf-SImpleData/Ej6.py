num = int(input("Por favor, indique el número a continuación (válidos números enteros mayores o iguales a uno (1): "))
if (num < 1):
    print("Número no válido.")
else:
    suma = 0
    for valor in range(num+1):
        suma = suma + valor
    print("La suma total es:", suma)
