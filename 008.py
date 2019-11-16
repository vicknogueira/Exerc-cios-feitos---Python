# 5. Tendo três valores inteiros (representados pelas variáveis A, B e C), calcule e apresente como
# resultado final o valor da soma dos quadrados dos três valores lidos.
A = int(input("Write a number for the letter A: "))
B = int(input("Write a number for the letter B: "))
C = int(input("Write a number for the letter C: "))
a = A ** 2
b = B ** 2
c = C ** 2
soma = a + b + c
print("The square of A is '{}' and B is '{}' and C is '{}' \nThe soma  square of letter A, B and C together is '{}' ".format(a, b, c, soma))
