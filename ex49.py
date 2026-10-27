dolares = float(input("Digite o valor em dólares: US$ "))
cotacao = float(input("Digite a cotação do dólar: R$ "))

reais = dolares * cotacao

print(f"Valor convertido: R$ {reais:.2f}")