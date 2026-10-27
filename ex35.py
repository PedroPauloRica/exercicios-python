tipo = input("Digite o tipo de carne: ").upper()
kg = float(input("Digite a quantidade em kg: "))
cartao = input("Pagamento com cartão Tabajara? (S/N): ").upper()

if tipo == "FILÉ DUPLO" or tipo == "FILE DUPLO":
    if kg <= 5:
        preco = 34.90
    else:
        preco = 35.80

elif tipo == "ALCATRA":
    if kg <= 5:
        preco = 44.90
    else:
        preco = 46.80

elif tipo == "PICANHA":
    if kg <= 5:
        preco = 66.90
    else:
        preco = 67.80

total = kg * preco

if cartao == "S":
    desconto = total * 0.05
    pagamento = "Cartão Tabajara"
else:
    desconto = 0
    pagamento = "Outro"

valor_final = total - desconto

print(f"Tipo de carne: {tipo}")
print(f"Quantidade: {kg} kg")
print(f"Preço total: R$ {total:.2f}")
print(f"Pagamento: {pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")