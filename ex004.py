n = input('Digite algo:')
print("O que você digitou é do tipo:", type(n))
print('Contém números e letras?', n.isalnum())
print('Esta escrito apenas em letras maiúsculas?', n.isupper())
print('Esta escrito apenas em letras minusculas?', n.islower())
print('Esta escrito em Decimal?', n.isdecimal())
print('Esta escrito apenas em letras', n.isalpha())
# Programa que verifica o tipo de um dado inserido pelo usuário