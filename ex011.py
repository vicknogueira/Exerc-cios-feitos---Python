largura = float(input("Qual o comprimento de sua parede?"))
altura = float(input('Qual a altura de sua parede?'))
area = largura * altura
tinta = area / 2
print("Sua parede tem dimensões de {} x {} e a sua área é de {:.2f}m²".format(largura, altura, area))
print("Para pintar a sua parede, você precisará de {:.2f}L de tinta".format(tinta))

# Programa que calcula a área de uma parede e mostra quantos Litros (L) de tinta será preciso para pintá-la
# OBS: A cada 2m² de parede é preciso de 1L de tinta
