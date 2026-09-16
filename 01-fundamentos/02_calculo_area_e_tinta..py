# Cálculo da área da parede e da quantidade de tinta

largura = float(input("Qual é a largura da parede, em metros? "))
altura = float(input("Qual é a altura da parede, em metros? "))

area = largura * altura
litros_tinta = area / 4

print(f"\nÁrea total da parede: {area:.2f} m²")
print(f"Quantidade de tinta necessária: {litros_tinta:.2f} litros")