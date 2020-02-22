valores = []
while True:
    valores.append(int(input('digite um numero: ')))
    resp = str(input('quer continuar? [S/N] ')).strip().lower()
    while resp not in 'ns':
        print('resposta invalida.tente novamente!')
        resp = str(input('quer continuar? [S/N] ')).strip().lower()
    if resp == 'n':
        break
print(f'foram digitados {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')
if 5 not in valores:
    print('o numero 5 não faz parte da lista')
else:
    print('o numero 5 faz parte da lista')
