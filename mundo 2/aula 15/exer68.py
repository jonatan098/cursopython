#JOGO DE PAR OU IMPAR
from random import randint
cont = 0
while True:
    comput = randint(0, 10)
    j1 = int(input('digite um valor: '))
    tot = j1 + comput
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I] ')).upper().strip()[0]
    print(f'voce jogou {j1} e o computador {comput}. total de {tot}', end=' ')
    print('deu PAR' if tot%2 == 0 else 'deu IMPAR')
    if tipo == 'P':
        if tot%2 == 0:
            print('VOCE VENCEU!')
            cont+=1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if tot%2 == 1:
            print('VOCE VENCEU!')
            cont+=1
        else:
            print('VOCE PERDEU!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER! voce venceu {cont} vezes.')