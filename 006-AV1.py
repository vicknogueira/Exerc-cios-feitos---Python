#6) Tendo como base o algoritmo abaixo, assinale a alternativa que corresponda ao valor de "num" logo após sua execução,
# num recebe 85
num = 85
if num < 40:
    num += 5
    print("Novo número é", num)
else:
    if num < 70:
        num *= 7
        print("Novo número é", num)
    else:
        num -= 3
        print("Novo número é", num)
# Resposta é 82