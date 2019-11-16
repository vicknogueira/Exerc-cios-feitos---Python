def main():
    tabuada = int(input("Digite one Number:"))
    print("A tabuada do {} is this:".format(tabuada))
    print("-"*12)
    for cont in range(0,11):
        n = tabuada * cont
        print("{} x {} = {} ".format(tabuada, cont, n))
    print("-"*20)
main()

# Programa que faz a tabuada (esse eu fiz sozinha :D)