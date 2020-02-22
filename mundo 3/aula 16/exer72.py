#Número por Extenso
numb = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
        'treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:   
    while True:
        user = int(input('digite um numero entre zero e vinte: '))
        if 0 <= user <= 20:
            break 
        print('tente novamente.', end='')
    print(f'voce digitou o número {numb[user]}')
    next = str(input('voce quer continuar [S/N]: ')).strip().upper()
    if next == 'N':
        break