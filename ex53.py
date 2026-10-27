quantidade_impares = 0

while True:
    numero = int(input("Digite um número inteiro (-999 para parar): "))

    if numero == -999:
        break

    if numero % 2 != 0:
        quantidade_impares += 1

print(f"Quantidade de números ímpares: {quantidade_impares}")