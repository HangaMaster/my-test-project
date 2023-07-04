capital = int(input("Introduzca el capital a invertir: "))
interes = float(input("Introduzca el interés en %: "))
anos = int(input("Introduzca el plazo de inversión en años: "))
beneficio = 0
for num in range(anos):
    calculo = float((capital * interes)/100)
    beneficio = float(beneficio + calculo)
print("El beneficio total a obtener es:", beneficio)
