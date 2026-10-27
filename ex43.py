moedas_1 = int(input("Quantidade de moedas de 1 centavo: "))
moedas_5 = int(input("Quantidade de moedas de 5 centavos: "))
moedas_10 = int(input("Quantidade de moedas de 10 centavos: "))
moedas_25 = int(input("Quantidade de moedas de 25 centavos: "))
moedas_50 = int(input("Quantidade de moedas de 50 centavos: "))
moedas_100 = int(input("Quantidade de moedas de 1 real: "))

total_centavos = (
    moedas_1
    + moedas_5 * 5
    + moedas_10 * 10
    + moedas_25 * 25
    + moedas_50 * 50
    + moedas_100 * 100
)

print(f"Total economizado: R$ {total_centavos / 100:.2f}")