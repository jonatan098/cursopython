#JOGO DE ADIVINHAÇÃO 2.0
from random import randint
comput = randint(0, 10)
print('vou pensar em um numero entre 0 e 10 tente adivinhar')
acertou = False
erro = 0
while not acertou:
    player = int(input('qual o numero: '))
    erro += 1
    if comput == player:
        acertou = True
    else:
        if player < comput:
            print('mais...tente novamnete.')
        elif player > comput:
            print('menos...tente novamente.')
print(f'acertou com {erro} tentativas. PARABÉNS!!!')