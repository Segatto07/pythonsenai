potencia = float(input("Indique a potência do chuveiro em (w) "))
tensao = float(input("Indique a tensão da instalação (127v or 220v)"))

if potencia <= 0 or tensao <= 0:
    print("Infome o valor correto que seja <= a 0")

else:
    corrente = potencia / tensao 

    corrente_margem = corrente * 1.10

    disjuntores = [32, 40, 50, 63]

    disjuntor = None

for valor in disjuntores:
    if valor <= corrente_margem:
        disjuntor = valor
    break

print(f"Potência do chuveiro: {potencia:.0f} W")
print(f"tensão da instalação: {tensao:.0f} v")
print(f"Corrente calculada: {corrente_margem:.2f} A")
print(f"Corrente com 10% de margem: {corrente_margem:.2f} A")

    

