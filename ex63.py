quantidade = int(input("Quantos números você deseja informar? "))

if quantidade <= 0:
    print("Informe uma quantidade maior que zero.")
else:
    numeros = []

    for i in range(1, quantidade + 1):
        numero = float(input(f"Digite o {i}º número: "))
        numeros.append(numero)

    print(f"Menor valor: {min(numeros)}")
    print(f"Maior valor: {max(numeros)}")
    print(f"Soma dos valores: {sum(numeros)}")