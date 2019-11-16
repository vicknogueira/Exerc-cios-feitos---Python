def main():
    pessoas = 0
    for cont in range(1, 11):
        idade = int(input("Digite a idade da {}ª:".format(cont)))
        if idade >= 18:
            pessoas += 1
    print("São maiores de 18 anos: \n {} pessoas".format(pessoas))

main()
# Programa que detecta quantas pessoas são maiores de 18 anos