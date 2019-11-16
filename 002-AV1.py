#2) Tendo como base o algoritmo
p = 15
if p == 0:
    p -= 3
else:
    if p % 3 == 0:
        p = p * 2
    else:
        p = p + 5
print("Novo número =", p)