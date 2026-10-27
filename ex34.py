litros = float(input("Digite a quantidade de litros: "))
combustivel = input("Digite o combustível (A - Álcool / G - Gasolina): ").upper()

if combustivel == "A":
    preco = 1.90

    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif combustivel == "G":
    preco = 2.50

    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

else:
    print("Combustível inválido")
    preco = 0
    desconto = 0

if preco > 0:
    total = litros * preco
    valor_desconto = total * desconto
    valor_final = total - valor_desconto

    print(f"Valor a pagar: R$ {valor_final:.2f}")