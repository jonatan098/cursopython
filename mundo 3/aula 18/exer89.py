cad = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    cad.append([nome, [nota1, nota2], media])
    resp = str(input('quer continuar? [S/N]')).strip().lower()
    if resp == 'n':
        break
    else:
        while resp not in 'ns':
            print('resposta invalida.tente novamente!!')
            resp = str(input('quer continuar? [S/N]')).strip().lower()
print('-='*30)
print(f'{"no":<4}{"nome":<10}{"media":>8}')
print('-'*26)
for i, a in enumerate(cad):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-'*26)
    user = int(input('mostrar a nota de qual aluno?(999 interompe): '))
    if user == 999:
        break
    if user <= len(cad) -1:
        print(f'notas de {cad[user][0]} são {cad[user][1]}')
print('<<<< VOLTE SEMPRE >>>>')