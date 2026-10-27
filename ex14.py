num_conta = str(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))

saldo_atual = saldo - debito + credito

if saldo >= 0:
    print("Saldo Positivo")

else:
    print("Saldo negativo")
