lista = ('lapis',1.75,'borracha',2,'caderno',15.90,'estojo',25)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for c in lista:
    if lista.index(c)%2 == 0:
        print(f'{c:.<30}', end='')
    else:
        print(f'R${c:>7.2f}')
print('-'*40)