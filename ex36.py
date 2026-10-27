sanduiche = int(input("Digite o código do sanduíche: "))
bebida = int(input("Digite o código da bebida: "))


if sanduiche == 100:
    preco_sanduiche = 11.20
elif sanduiche == 101:
    preco_sanduiche = 8.30
elif sanduiche == 102:
    preco_sanduiche = 11.50
elif sanduiche == 103:
    preco_sanduiche = 16.20

if bebida == 201:
    preco_bebida = 6.00
elif bebida == 202:
    preco_bebida = 7.50
elif bebida == 203:
    preco_bebida = 4.70

total = preco_sanduiche + preco_bebida

print(f"Valor a pagar: R$ {total:.2f}")