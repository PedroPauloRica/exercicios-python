pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
medias = int(input("Digite a quantidade de camisetas médias: "))
grandes = int(input("Digite a quantidade de camisetas grandes: "))

total = (pequenas * 10) + (medias * 12) + (grandes * 15)

print(f"Valor total da compra: R$ {total:.2f}")