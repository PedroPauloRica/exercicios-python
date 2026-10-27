divida = float(input("Digite o valor da dívida: R$ "))

parcelas = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

print("\nDívida total | Juros | Parcelas | Valor da parcela")

for p, percentual in parcelas:
    juros = divida * percentual / 100
    divida_total = divida + juros
    valor_parcela = divida_total / p

    print(
        f"R$ {divida_total:.2f} | "
        f"R$ {juros:.2f} | "
        f"{p}x | "
        f"R$ {valor_parcela:.2f}"
    )