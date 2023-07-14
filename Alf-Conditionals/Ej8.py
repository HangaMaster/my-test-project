try:
    score = float(input("Introduce la puntuación del empleado: "))
    if score == (0.0):
        print("Beneficios obtenidos: 0€.")
    elif score == 0.4:
        print("Beneficios obtenidos: " + str(2400 * 0.4) + "€.")
    elif score >= 0.6:
        print("Beneficios obtenidos: " + str(2400 * score) + "€.")
    else:
        print("Valor no válido.")
except ValueError:
    print("Valor no válido.")
