preco = float(input("Digite o preço do produto: "))

desconto = preco * 0.10
novo_preco = preco - desconto

print(f"Novo preço: R$ {novo_preco:.2f}")