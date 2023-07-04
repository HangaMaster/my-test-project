capital = float(input("Introduzca el capital a ingresar en su cuenta de ahorro: "))
for i in range(3):
    ahorro = (capital * 4) / 100
    capital = ahorro + capital
    print("La cantidad ahorrada al final del año", i+1, "es de: ", round(capital,2))