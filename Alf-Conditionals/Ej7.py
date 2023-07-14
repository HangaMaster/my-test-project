try:
    rent = float(input("Introduce tu renta anual: "))
    if rent < 10000:
        imp = 5
    elif rent <= 20000:
        imp = 15
    elif rent <= 35000:
        imp = 20
    elif rent <= 60000:
        imp = 30
    else:
        imp = 45
    print("Tu tipo impositivo es: " + str(imp) + "%")
    print("Tienes que pagar: " + str(round(rent * (imp / 100), 2)) + "€")
except ValueError:
    print("Valor no válido.")
