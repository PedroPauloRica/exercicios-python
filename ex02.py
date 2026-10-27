nome = str(input("Digite seu nome: "))

n1 = int(input("Digite a nota do primeiro semestre: "))
n2 = int(input("Digite a nota do segundo semestre: "))
n3 = int(input("Digite a nota do terceiro semestre: "))
n4 = int(input("Digite a nota do quarto semestre: "))

print(f"Nome: {nome}")
print(f"Bimestre 1º: {n1} \nBimestre 2º: {n2} \nBimestre 3º: {n3} \nBimestre 4º: {n4}")

media = (n1 + n2 + n3 + n4) / 4

print(f"A sua média foi: {media}")