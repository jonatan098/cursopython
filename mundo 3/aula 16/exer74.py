from random import randint
numbs = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'os numeros escolhidos foram: ', end='')
for n in numbs:
    print(f'{n} ', end='')
print(f'\no maior numero escolhidos foi {max(numbs)}')
print(f'o menor numero escolhido foi {min(numbs)}')