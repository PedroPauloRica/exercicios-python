cidades = []
veiculos = []
acidentes = []
acidentes_cidades_pequenas = []

for i in range(5):
    codigo = input("\nCódigo da cidade: ")
    quantidade_veiculos = int(input("Quantidade de veículos: "))
    quantidade_acidentes = int(input("Quantidade de acidentes: "))

    cidades.append(codigo)
    veiculos.append(quantidade_veiculos)
    acidentes.append(quantidade_acidentes)

    if quantidade_veiculos < 2000:
        acidentes_cidades_pequenas.append(quantidade_acidentes)

maior = max(acidentes)
menor = min(acidentes)

print("Maior número de acidentes:", maior)
print("Cidade:", cidades[acidentes.index(maior)])

print("Menor número de acidentes:", menor)
print("Cidade:", cidades[acidentes.index(menor)])

print("Média de veículos:", sum(veiculos) / 5)

if len(acidentes_cidades_pequenas) > 0:
    media = sum(acidentes_cidades_pequenas) / len(acidentes_cidades_pequenas)
    print("Média de acidentes nas cidades com menos de 2.000 veículos:", media)
else:
    print("Nenhuma cidade possui menos de 2.000 veículos")