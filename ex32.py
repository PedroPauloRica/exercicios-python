saque = int(input("Digite o valor do saque: "))

if saque < 10 or saque > 600:
    print("O saque tem que ser entre R$ 10 e R$ 600.")

else: 
    valor = saque

    nota100 = valor // 100
    valor = valor % 100

    nota50 = valor // 50
    valor = valor % 50

    nota10 = valor // 10
    valor = valor % 10

    nota5 = valor // 5
    valor = valor % 5

    nota1 = valor // 1

    print(f"Saque de R$ {saque}")
    print(f"Notas de R$ 100: {nota100}")
    print(f"Notas de R$ 50: {nota50}")
    print(f"Notas de R$ 10: {nota10}")
    print(f"Notas de R$ 5: {nota5}")
    print(f"Notas de R$ 1: {nota1}")


saque = int(input("Qual o valor deseja sacar?\n: "))
valor = saque
nota_cem = nota_cinquenta = nota_dez = nota_cinco = nota_um = 0
if saque < 10 or saque > 600:
    print("Fim, valores muito altos ou baixos")
    exit()
else:
    if saque >= 100:
        while saque >= 100:
            saque = saque - 100
            nota_cem += 1

    if saque >= 50:
        while saque >= 50:
            saque = saque - 50
            nota_cinquenta += 1

    if saque >= 10:
        while saque >= 10:
            saque = saque - 10
            nota_dez += 1

    if saque >= 5:
        while saque >= 5:
            saque = saque -5
            nota_cinco += 1

    if saque >= 1:
        while saque >= 1:
            saque = saque - 1
            nota_um += 1

print(f"Para sacar {valor} reais, vou te dar {nota_cem} nota(s) de 100, {nota_cinquenta} nota(s) de 50, {nota_dez} nota(s) de 10, {nota_cinco} nota(s) de 5, {nota_um} notas(s) de 1")