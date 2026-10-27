nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (F/M): ").strip().upper()
estado_civil = input("Digite seu estado civil: ").strip().upper()

print(f"\nNome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Há quantos anos você é casada? "))
    print(f"Tempo de casada: {tempo_casada} ano(s)")