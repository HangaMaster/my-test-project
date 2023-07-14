age = int(input("Introduce tu edad: "))
inc = float(input("Introduce tus ingresos mensuales: "))
if age >= 18 and inc > 1000:
    print("Tienes que pagar.")
else:
    print("No tienes que pagar.")
