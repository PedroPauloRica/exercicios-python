nome = str(input("Digite seu nome: "))
disciplina = str(input("Digite o nome da disciplina: "))


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))


media = (n1 + n2 + n3) / 3

if media >= 6:
    print(f"Nome: {nome}\nDisciplina: {disciplina}\nSituação final: Aprovado")

else:
    print(f"Nome: {nome}\n Disciplina: {disciplina}\nSituação final: Reprovado") 