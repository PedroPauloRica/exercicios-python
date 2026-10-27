num = int(input("Digite um número: "))

if num > 100:
    print("O número digitado é maior do que 100")
    num2 = int(input("Digite outro número: "))
    if num > 150:
        print('Digite outro número maior do que 150')

elif num < 100:
    print("O número digitado é menor do que 100")

else:
    print("O número digitado é igual a 100")


