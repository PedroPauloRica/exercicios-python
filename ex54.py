quantidade_50 = 0

while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))

    if numero == 0:
        break

    if numero == 50:
        quantidade_50 += 1

print(f"O número 50 foi informado {quantidade_50} vezes")