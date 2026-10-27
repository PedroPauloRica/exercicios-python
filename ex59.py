numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

print(f"Números entre {menor} e {maior}:")

if maior - menor <= 1:
    print("Não temnúmeros inteiros entre eles")
else:
    for numero in range(menor + 1, maior):
        print(numero)