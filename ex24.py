sanduiches = int(input("Digite a quantidade de sanduíches: "))

queijo = sanduiches * 100
presunto = sanduiches * 50
carne = sanduiches * 100

queijo_kg = queijo / 1000
presunto_kg = presunto / 1000
carne_kg = carne / 1000

print(f"Queijo: {queijo_kg:.2f} kg")
print(f"Presunto: {presunto_kg:.2f} kg")
print(f"Carne: {carne_kg:.2f} kg")