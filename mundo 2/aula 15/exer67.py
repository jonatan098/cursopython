#TABUADA v3.0
while True:
    n = int(input('quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*20)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-'*20)
print('Programa encerrado. Volte sempre!')
