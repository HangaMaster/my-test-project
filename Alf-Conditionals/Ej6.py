name = input("Introduce tu nombre: ")
gender = input("Introduce tu sexo (H/M): ")
if (gender == "M" and name.lower() < "m") or (gender == "H" and name.lower() > "n"):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es: " + grupo)
