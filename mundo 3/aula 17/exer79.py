valores = []
while True:
    n = int(input('digite um numero: '))
    if n not in valores:
        valores.append(n)
        print('valor adicionado com sucesso!') 
    else:
        print('valor duplicado! não vou adicionar')
    resp = str(input('quer continuar [S/N]: ')).strip().upper()
    while resp not in 'NS':
        print('resposta invalida.tente novamente!')
        resp = str(input('quer continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
valores.sort()
print(valores)