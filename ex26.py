preco = float(input("Digite o preço de aquisição: "))

if preco < 50:
    valor_venda = preco + (preco * 0.45)
else:
    valor_venda = preco + (preco * 0.30)

print(f"Valor de venda: R$ {valor_venda:.2f}")