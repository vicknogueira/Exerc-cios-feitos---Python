# 2. Tendo a base e a altura de um triângulo, calcule sua área por meio da fórmula: area = (base x altura)/2
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a base do triângulo: "))
area = (base * altura)/2
print("O triângulo possui uma altura de {}cm e uma base de {}cm \nSua área é de {}cm ".format(altura, base, area))