print("CARDÁPIO")
print("1 - Bife acebolado: R$ 15,00")
print("2 - Lasanha: R$ 25,00")
print("3 - Frango grelhado: R$ 20,00")
print("4 - Strogonoff: R$ 23,00")
print("5 - Peixe frito: R$ 28,00")

opcao = int(input("Escolha um prato: "))

if opcao == 1:
    prato = "Bife acebolado"
    valor = 15.00
elif opcao == 2:
    prato = "Lasanha"
    valor = 25.00
elif opcao == 3:
    prato = "Frango grelhado"
    valor = 20.00
elif opcao == 4:
    prato = "Strogonoff"
    valor = 23.00
elif opcao == 5:
    prato = "Peixe frito"
    valor = 28.00
else:
    prato = ""
    print("Opção inválida.")

if prato:
    resposta = input("Aceita pagar 10% de gorjeta? (S/N): ").strip().upper()

    if resposta == "S":
        gorjeta = valor * 0.10
    elif resposta == "N":
        gorjeta = 0
    else:
        gorjeta = None
        print("Resposta inválida. Digite S ou N.")

    if gorjeta is not None:
        total = valor + gorjeta

        print(f"\nPrato: {prato}")
        print(f"Valor do prato: R$ {valor:.2f}")
        print(f"Gorjeta: R$ {gorjeta:.2f}")
        print(f"Valor final: R$ {total:.2f}")