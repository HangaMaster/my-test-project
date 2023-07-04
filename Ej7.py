estatura = float(input("Por favor, indique su estatura en metros: "))
peso = float(input("A continuación, indique su peso en kilos: "))
imc = peso / estatura
round(imc, 2)
print("Tu IMC (Índice de Masa Corporal) es: ", round(imc, 2))

