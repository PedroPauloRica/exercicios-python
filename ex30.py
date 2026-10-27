peso = float(input("Digite o peso do peixe: "))
excesso = 0

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print(f"Seu peixe pesa {peso} e ultrapassou o regulamento de São Paulo que estabelece o peso em 50 quilos, e por isso deve pagar uma multa de R$ 4,00 por quilo excedente.")
    print(f"Como seu peixe passou {excesso} quilo do limite pagará o valor de R${multa}")

else:
    print(f"Seu peixe está pesando {peso:.0f} estando dentro do regulamentl de 50 quilos, está liberado.")

