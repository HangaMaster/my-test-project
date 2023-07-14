# Ejercicio: Fizz Buzz de 100 elementos
for num in range(101):
    resul1 = num % 3
    resul2 = num % 5
    if resul1 == 0:
        Fizz = "Fizz"
    else:
        Fizz = ""
    if resul2 == 0:
        Buzz = "Buzz"
    else:
        Buzz = ""
    if (num == 0) or (resul1 != 0 and resul2 != 0):
        print(num)
    else:
        print(str(Fizz) + str(Buzz))
