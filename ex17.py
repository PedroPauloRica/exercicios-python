salario = float(input("Digite seu salário: "))

if salario <= 280.00:
    n1 = salario * (20 /100)
    novo = salario + n1
    print(f"Seu salário é de {salario} e recebeu um aumento de 20%, recebendo no total {novo} ") 

elif salario >= 281.00 and salario <= 700.00:
    n1 = salario * (15/100)
    novo = salario + n1
    print(f"Seu salário é de {salario} e recebeu um aumento de 15%, recebendo no total {novo} ") 

elif salario >= 701.00 and salario <= 1500.00:
    n1 = salario * (10/100)
    novo = salario + n1
    print(f"Seu salário é de {salario} e recebeu um aumento de 10%, recebendo no total {novo} ") 

elif salario >= 1501.00:
    n1 = salario * (5/100)
    novo = salario + n1
    print(f"Seu salário é de {salario} e recebeu um aumento de 5%, recebendo no total {novo} ")  