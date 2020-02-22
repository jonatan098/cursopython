from time import sleep
valor1 = int(input('digite o primeiro valor: '))
valor2 = int(input('digite o segundo valor: '))
respos = 0
while respos != 5:
    print(""""[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa""")
    respos = int(input('o que quer fazer: '))
    if respos == 1:
        print(f'o resultado da soma de {valor1} + {valor2} = {valor1 + valor2} ')
    elif respos == 2:
        print(f'o resultado da multiplicação de {valor1} X {valor2} = {valor1 * valor2}')
    elif respos == 3:
        if valor1 > valor2:
            print(f'o maior valor digitado foi {valor1}')
        else:
            print(f'o maoir valor digitado foi {valor2}')
    elif respos == 4:
        print('digite novos numeros')
        valor1 = int(input('digite o primeiro valor: '))
        valor2 = int(input('digite o segundo valor: '))
    elif respos == 5:
        print('finalizando...')
    else:
        print('invalido tente novamente')
    print('=-='*20)
    sleep(1)
print('volte sempre')