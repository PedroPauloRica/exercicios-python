n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

op = int(input("Qual operação deseja realizar? \n1- Par ou Ímpar \n2- Positivo ou Negativo \n3- Inteiro ou decimal \nR:"))


match op:
    case 1:
        if n1.is_integer():
            if n1 % 2 == 0:
                print("o primeiro número digitado é par")

            else:
                print("O primeiro número é ímpar")

        else:
            print("Não posso calcular número decimal")
        
        if n2.is_integer():
            if n2 % 2 == 0:
                print("o segundo número digitado é par")

            else:
                print("O segundo número é ímpar")

        else:
            print("Não posso calcular número decimal")
        
        

    case 2:
        if n1 >= 0:
            print("O primeiro número digitado é positivo")

        else:
            print("O primeiro número digitado é negativo")
        
        if n2 >= 0:
            print("O segundo número digitado é positivo")

        else:
            print("O segundo número digitado é negativo")

    case 3:
        if n1.is_integer():
            print("O primeiro número digitado é Inteiro")

        else:
            print("O primeiro número digitado é Decimal")
        
        if n2.is_integer():
            print("O segundo número digitado é Inteiro")

        else:
            print("O segundo número digitado é Decimal")


