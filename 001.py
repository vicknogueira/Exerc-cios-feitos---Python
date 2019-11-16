#  1. Considerando 2 números inteiros, faça a soma, subtração e multiplicação. Por fim, mostre os resultados
n1 = int(input("Digite um número: "))
n2 = int(input("digite outro número:"))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
print('A soma entre os números {} e {} é {}, a multiplicação é {} e a subtração é {}.'.format(n1, n2, soma, mult, sub))