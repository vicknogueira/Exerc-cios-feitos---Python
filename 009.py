# Escreva um algoritmo que leia um número inteiro qualquer, avalie e mostre na tela se o número é zero, múltiplo de 3 ou não.
n = int(input('Write a number: '))
if n == 0:
    print("The number que você escreveu foi 0 :D")
if n % 3 == 0:
    print("The number {} is multiplo de 3 :D ".format(n))
else:
    print('Deculpe o número que escreveu não é múltiplo de 3 ou 0 :(')