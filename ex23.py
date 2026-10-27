frangos = int(input("Digite a quantidade de frangos: "))

custo_chip = 4.00
custo_alimento = 3.50 * 2

custo_por_frango = custo_chip + custo_alimento
custo_total = frangos * custo_por_frango

print(f"Gasto total: R$ {custo_total:.2f}")