heavy = light = 0
everyone = []
dados = []
while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    if len(everyone) == 0:
        heavy = light = dados[1]
    elif dados[1] >= heavy:
        heavy = dados[1]
    elif dados[1] <= light:
        light = dados[1]
    everyone.append(dados[:])
    dados.clear()
    resp = str(input('quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        print('resposta invalida.tente novamente')
        resp = str(input('quer continuar [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'total de pessoas cadrastradas foram {len(everyone)}')
print(f'o maior peso foi de {heavy}kg peso de', end=' ')
for p in everyone:
    if heavy == p[1]:
        print(f'{p[0]}', end=', ')
print()
print(f'o menor peso foi de {light} peso de', end=' ')
for p in everyone:
    if light == p[1]:
        print(f'{p[0]}', end=', ')
print()
