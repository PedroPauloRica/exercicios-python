soma = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 5

print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")

