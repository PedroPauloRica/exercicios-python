preco = float(input("Digite o preço do produto: R$ "))

print("\nCondições de pagamento:")
print("1 - À vista em dinheiro ou Pix: 10% de desconto")
print("2 - À vista no cartão de crédito: 5% de desconto")
print("3 - Em duas vezes: preço normal")
print("4 - Em três vezes: acréscimo de 10%")

codigo = int(input("Escolha uma opção: "))

if codigo == 1:
    total = preco * 0.90
    print(f"Valor a pagar: R$ {total:.2f}")
elif codigo == 2:
    total = preco * 0.95
    print(f"Valor a pagar: R$ {total:.2f}")
elif codigo == 3:
    total = preco
    print(f"Valor a pagar: R$ {total:.2f}")
    print(f"2 parcelas de R$ {total / 2:.2f}")
elif codigo == 4:
    total = preco * 1.10
    print(f"Valor a pagar: R$ {total:.2f}")
    print(f"3 parcelas de aproximadamente R$ {total / 3:.2f}")
else:
    print("Condição de pagamento inválida")