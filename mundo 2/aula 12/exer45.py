from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
comput = randint(0,2)
print('''suas opções:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA''')
jog = int(input('qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*11)
print(f'computador jogou {itens[comput]}')
print(f'jogador jogou {itens[jog]}')
print('-='*11)
if comput == 0: #compudator jogou pedra
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR VENCE')
    elif jog == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif comput == 1: #compudator jogou papel
    if jog == 0:
        print('COMPUTADOR VENCE')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif comput == 2: #compudator jogou tesoura
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

