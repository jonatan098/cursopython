dados = {}
gols = []
dados['nome'] = str(input('nome: '))
partidas = int(input(f'quantas partidas {dados["nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'quantos gols na partida {p+1}: ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print('-='*30) 
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'o campo {k} tem valor {v}')
print('-='*30)
print(f'o jogador {dados["nome"]} fez em {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'  => na partida {i+1}, fez {v}')
print(f'foi um total de {dados["total"]} gols')