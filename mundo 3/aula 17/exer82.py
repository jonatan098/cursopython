valores = []
valoresimp = []
valorespar = []
while True:
    valores.append(int(input('digite um numero: ')))
    resp = str(input('quer continuar? [S/N] '))
    while resp not in 'SNns':
        print('resposta invalida.tente novamente!')
        resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for v in valores:
    if v%2 == 0:
        valorespar.append(v)
    else:
        valoresimp.append(v)
print(f'a lista completa é {valores}')
print(f'a lista de pares é {valorespar}')
print(f'a lista de impares é {valoresimp}')