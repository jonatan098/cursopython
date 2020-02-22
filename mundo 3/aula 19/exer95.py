galera = []
dados = {}
golsl = []
while True:
    dados['nome'] = str(input('nome: '))
    partidas = int(input(f'quantas partidas {dados["nome"]} jogou? '))
    for p in range(0, partidas):
        golsl.append(int(input(f'quantos gols na partida {p+1}: ')))
    dados['gols'] = golsl[:]
    dados['total'] = sum(golsl)
    golsl.clear()
    galera.append(dados.copy())
    while True:
        resp = str(input('quer continuar? [s/n] ')).lower()[0].strip()
        if resp in 'sn':
            break
    if resp == 'n':
        break
print('-='*30)
print('cod ', end='') 
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*46)
for k, v in enumerate(galera):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
print('-'*46)
while True:
    user = int(input('mostrar dados de qual jogador? [999 termina] '))
    if user == 999:
        break
    if user >= len(galera):
        print('ERRO. não existe jogador com esse codigo!!')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {galera[user]["nome"]}')
        for i, g in enumerate(galera[user]['gols']):
            print(f'   na partida {i} fez {g} gols')
    print('-'*40)
print('<<<<VOLTE SEMPRE>>>>')