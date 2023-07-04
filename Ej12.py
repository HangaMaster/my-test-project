bread = int(input("Introduzca las barras de pan no vendidas durante el día de hoy: "))
normalcost = 3.49
offcost = 3.49 * 0.4
finalcost = bread * offcost
print("Barras de pan no vendidas:", bread, "\nDescuento aplicado a cada barra de pan:", round(offcost, 2), "€\nCoste de las barras no vendidas:", finalcost,"€")
