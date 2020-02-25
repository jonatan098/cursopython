from time import sleep
from random import randint
def sortear():
    print('sorteando 5 valores para lista: ', end='')
    for v in range(0,5):
        rand = randint(0,100)
        num.append(rand)
        print(rand, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
def somepar():
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'somando os valores pares de {num} temos {soma}')
#main cod
num = []
sortear()
somepar()
