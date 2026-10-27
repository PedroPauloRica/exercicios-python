latas = int(input("Quantidade de latas de 350 ml: "))
garrafas_600 = int(input("Quantidade de garrafas de 600 ml: "))
garrafas_2 = int(input("Quantidade de garrafas de 2 litros: "))

total_litros = (latas * 0.350) + (garrafas_600 * 0.600) + (garrafas_2 * 2)

print(f"Total comprado: {total_litros:.2f} litros")