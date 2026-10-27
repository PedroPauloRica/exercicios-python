pop_a = 80000
pop_b = 200000
anos = 0

while pop_a < pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    anos += 1

print(f"Serão necessários {anos} anos.")
print(f"país A: {pop_a:.0f} habitantes")
print(f"país B: {pop_b:.0f} habitantes")

