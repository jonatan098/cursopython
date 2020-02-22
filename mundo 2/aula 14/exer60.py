#calculando fatorial
'''from math import factorial
numb = int(input('digite um numero: '))
f = factorial(numb)
print(f'o fatorial de {numb} é {f}')'''
numb = int(input('digite um numero para calcular seu fatorial: '))
c = numb
fator = 1
while c > 0:
    print(f'{c} ',end='')
    print('X ' if c > 1 else '= ',end='')
    fator *= c
    c -= 1
print(f'{fator}')