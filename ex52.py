quantidade = 0

while True:
    numero = float(input("Digite um número (-1 para parar): "))

    if numero == -1:
        break

    quantidade += 1

print(f"Quantidade de números digitados: {quantidade}")