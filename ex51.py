soma = 0

while True:
    numero = float(input("Digite um número (-999 para parar): "))

    if numero == -999:
        break

    soma += numero

print(f"Soma dos números: {soma}")