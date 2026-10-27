altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M/F): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

else:
    print("Sexo inválido")