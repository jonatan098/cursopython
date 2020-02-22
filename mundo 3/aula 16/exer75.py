user = (int(input('digite um numero: ')), int(input('digite outro numero: ')), 
        int(input('digite mais um numero: ')), int(input('digite o último numeor: ')))
print(f'voce digitou os valores {user}')
print(f'o valor 9 apareceu {user.count(9)} vezes')
print(f'os valores pares digitados foram ', end='')
for n in user:
    if n % 2 == 0:
        print(n, end=' ')
if 3 in user:
    print(f'\no valor 3 apareceu na {user.index(3)+1}ª posição')
else:
    print('o valor 3 não foi digitado')