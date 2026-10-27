numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Não é possível calcular fatorial de um número negativo")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i

    print(f"{numero}! = {fatorial}")
    