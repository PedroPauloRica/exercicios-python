numeros = []

for i in range(1, 21):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

print(f"Menor número: {min(numeros)}")
print(f"Maior número: {max(numeros)}")