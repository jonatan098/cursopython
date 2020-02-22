#DESCUBRE SE UM NUMERO E PRIMO OU NÃO
numb = int(input('digite um numero: '))
cont = 0
for c in range(1,numb+1):
    if numb % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m o numero {numb} foi divisível {cont} vezes')
if cont == 2:
    print('e por isso ele É PRIMO')
else:
    print('e por isso ele NÃO É PRIMO!!!')
