import random

print('Bem Vindo Ao Seu Gerador De Senhas!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&^().,0123456789'

number = input ('Quantidade de senha para gerar: ')
number = int(number)

lenght = input('Coloque comprimento da sua senha: ')
lenght = int(lenght)

print ('aqui esta suas senhas: ')

for pwd in range(number):
    senhas = ''
    for c in range(lenght):
        senhas += random.choice(chars)
    print(senhas)

