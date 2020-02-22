#JOGO DE ADIVINHAÇÃO
from random import randint
from time import sleep
comput = randint(0,5) #faz o computador "PENSAR"
print('\033[0;34;0m-=-\033[m' *20)
print('vou pensar e um numero entre 0 e 5. tente adivinhar...')
print('\033[0;34;0m-=-\033[m' *20)
jog = int(input('em qual numero eu pensei? ')) #jogador tenta adivinhar
print('\033[0;30;0mPROCESSANDO...')
sleep(3)
if comput == jog:
    print('\033[1;33;0mVOCÊ VENCEU!\033[m')
else:
    print(f'\033[7;31;0mVOCÊ PERDEU!\033[m,o numero que pensei foi {comput} e não {jog}')

