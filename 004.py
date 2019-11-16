# 4. Tendo como base o salário de um funcionário, faça o acréscimo de 20% sobre seu valor e exiba-o.
# DICA: para fazer o acréscimo, multiplique o valor do salário por 1,20.
salario = float(input("Qual seu salario? "))
acrescimo = salario * 1.20
print("O seu salário é R${:.2f}  e com o acréscimo de 20% seu novo salário será R${:.2f}".format(salario, acrescimo))