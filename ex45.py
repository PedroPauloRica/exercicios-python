ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento

if idade_anos < 0:
    print("O ano de nascimento não pode ser maior que o ano atual.")
else:
    idade_meses = idade_anos * 12
    idade_dias = idade_anos * 365
    idade_semanas = idade_dias // 7

    print(f"Idade em anos: {idade_anos}")
    print(f"Idade aproximada em meses: {idade_meses}")
    print(f"Idade aproximada em dias: {idade_dias}")
    print(f"Idade aproximada em semanas: {idade_semanas}")