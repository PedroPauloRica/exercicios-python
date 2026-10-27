paes = int(input("Digite quantidade de pães vendidos: "))
broas = int(input("Digite quantidade de broas vendidas: "))

total_paes = paes * 1
total_broas = broas * 3.50

total = total_paes + total_broas
poupanca = total * 0.10

print(f"Total arrecadado: R$ {total:.2f}")
print(f"Valor para guardar na poupança: R$ {poupanca:.2f}")