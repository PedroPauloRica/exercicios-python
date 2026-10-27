km = float(input("Digite a distância da viagem em km: "))
consumo = float(input("Digite o consumo do carro em km: "))
preco = float(input("Digite o preço de combustível  por litro: "))

litros = km / consumo
custo = litros * preco

print(f"O custo da viagem é R$ {custo:.2f}")
