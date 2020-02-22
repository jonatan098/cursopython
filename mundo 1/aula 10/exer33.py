n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
"""if n1 > n2 and n1 > n3:
   print(f'o maior numero e {n1}')
if n2 > n1 and n2 > n3:
    print(f'o maior numero e {n2}')
if n3 > n1 and n3 > n2:
    print(f'o maior numero e {n3}')
if n1 < n2 and n1 < n3:
    print(f'o menor numero e {n1}')
if n2 < n1 and n2 < n3:
    print(f'o menor numero e {n2}')
if n3 < n1 and n3 < n2:
    print(f'o menor numero e {n3}')"""
#verificando maior numero
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f'o maior numero digitado foi {maior}')
#verificando menor numero
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f'o menor numero digitado foi {menor}')
