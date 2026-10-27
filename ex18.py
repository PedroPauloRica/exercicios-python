valor = float(input("Digite o valor da sua hora: "))

quantidade = int(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = (valor * quantidade)

if salario_bruto <= 900.00:
    desconto = 0
    p1 = "Isento"

elif salario_bruto <= 1500.00:
    desconto = salario_bruto * (5/100)
    p1 = "5%"

elif salario_bruto <= 2500.00:
    desconto = salario_bruto * (10/100)
    p1 = "10%"

else:
    desconto = salario_bruto * (20/100)
    p1 = "20%"

inss = salario_bruto * (3/100)
fgts = salario_bruto * (11/100)

total_descontos = desconto + inss

salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor} * {quantidade}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({p1})                  : R$ {desconto:.2f}")
print(f"(-) Sindicato (3%)            : R$ {inss:.2f}")
print(f"FGTS (11%)                     : R$ {fgts:.2f}")
print(f"Total de descontos            : R$ {total_descontos:.2f}")
print(f"Salário Líquido                : R$ {salario_liquido:.2f}")

