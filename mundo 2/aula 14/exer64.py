#TRATANDO VÁRIOS VALORES
total = soma = numb = 0
numb = int(input('digite o numero [999 para parar]: '))
while numb != 999:
    total += 1
    soma = numb + soma
    numb = int(input('digite o numero [999 para parar]: '))
print(f'voce digitou {total} numeros e a soma entre eles é {soma}')