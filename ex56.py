livros = int(input("Quantos livros você comprou no bimestre? "))

if livros < 0:
    print("Quantidade inválida.")
else:
    if livros == 0:
        pontos = 0
    elif livros == 1:
        pontos = 5
    elif livros == 2:
        pontos = 15
    elif livros == 3:
        pontos = 30
    else:
        pontos = 60

    print(f"Você ganhou {pontos} pontos.")

    if 20 <= pontos <= 30:
        print("Brinde: uma Eco Bag ou uma caneta personalizada.")
    elif 35 <= pontos <= 60:
        print("Brinde: um livro de até R$ 30,00 ou uma luminária de cabeceira.")
    elif pontos > 65:
        print("Brinde: dois livros de até R$ 100,00 ou um power bank.")
    else:
        print("Sua pontuação não dá direito a um brinde.")