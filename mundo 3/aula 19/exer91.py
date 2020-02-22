from random import randint
from time import sleep
from operator import itemgetter
jog = {'jogador1': randint(1,6), 'jogador2': randint(1,6),
     'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = []
print('valores sordeados:')    
for k, v in jog.items():
    print(f'  o {k} tirou {v}')
    sleep(1)
ranking = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar {v[0]} com {v[1]}.')
    sleep(1)