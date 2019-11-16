# 1. Sabendo o peso e a altura de uma pessoa, calcule o IMC (índice de massa corpórea) por meio da
# fórmula: IMC = peso/(altura x altura).
peso = float(input("Digite o peso: "))
altura   = float(input('Digite a altura: '))
imc = peso/(altura * altura)
print("Seu IMC é ", imc)