from random import randint
from time import sleep
lista = []
temp = []
user = int(input('quantos palpites voce quer? '))
print('-='*30)
for l in range(0,user):
    for p in range(0,6):
        rand = randint(1,60)
        if rand not in temp:
            temp.append(rand)
        else:
            while True:
                rand = randint(1,60)
                if rand not in temp:
                    temp.append(rand)
                    break
    lista.append(temp[:])
    temp.clear()
    lista[l].sort()
    print(f'jogo{l+1}: {lista[l]}')
    print('-='*20)
    sleep(1)
print('BOM JOGO!!')