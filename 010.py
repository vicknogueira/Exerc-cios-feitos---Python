# Dados dois números inteiros m e n, verifique e mostre se eles são iguais. Caso não sejam, verifique e mostre qual é o maior deles.
m = int(input('Write a number: '))
n = int(input('Write a number: '))
if n > m:
    print("The number {} é maior que {}".format(n, m))
if m > n:
        print("The number {} é maior que {}".format(m, n))
else:
    print('Você escreveu two numbers iguais :D')