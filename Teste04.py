def main():
    impares = 0
    for cont in range(1, 6):
        n = int(input("Digite o {}ª número:".format(cont)))
        if n % 2 != 0:
            impares += 1
    print("Você digitou {} números impares".format(impares))

main()
# Programa que conta quantos números impares  que o usuário digitou