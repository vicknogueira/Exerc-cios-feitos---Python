salario = float(input("Qual o seu salário? R$ "))
aumento = salario + (salario * 15 / 100)
print("Seu salário anterior era R${:.2f} e agora com 15% de aumento seu novo salário é R${:.2f} :D".format(salario, aumento))