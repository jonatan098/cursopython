dados = {}
pasta = []
soma = media = 0
while True:
    dados['nome'] = str(input('nome: '))
    dados['sexo'] = str(input('sexo [F/M]: ')).upper()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO. por favor,digite apenas M ou F.')
        dados['sexo'] = str(input('sexo [F/M]: ')).upper()[0]
    dados['idade'] = int(input('idade: '))
    soma += dados['idade']
    pasta.append(dados.copy())
    while True:
        resp = str(input('quer continuar? [s/n] ')).lower()[0].strip()
        if resp in 'sn':
            break
    if resp == 'n':
        break
print('-='*30)
print(f'foram cadastradas {len(pasta)} pessoas.')
media = soma / len(pasta)
print(f'a media de idade do grupo é de {media:5.2f}')
print('as mulheres cadastradas foram ', end=' ')
for v in pasta:
    if v['sexo'] == 'F':
        print(f'{v["nome"]}', end=' ')
print()
print('lista das pessoas que estão acima da media: ')
for p in pasta:
    if p['idade'] >= media:
        print('   ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<<<< ENCERRADO>>>>')