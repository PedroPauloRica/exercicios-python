feminino_altura = 0
total_masculino = 0
masculino_bom = 0

for i in range(50):

    matricula = input("Digite a matrícula: ")
    sexo = input("Digite o sexo (M/F): ").upper()
    altura = float(input("Digite a altura em cm: "))
    status = int(input("Digite o status físico (1-Bom, 2-Regular, 3-Ruim): "))

    if sexo == "F" and altura > 170:
        feminino_altura += 1

    if sexo == "M":
        total_masculino += 1

        if status == 1:
            masculino_bom += 1

print(f"Quantidade de mulheres com mais de 170 cm: {feminino_altura}")

if total_masculino > 0:
    porcentagem = (masculino_bom / total_masculino) * 100
    print(f"Porcentagem de homens com status bom: {porcentagem:.2f}%")
else:
    print("Não foram cadastrados homens.")