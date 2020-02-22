#TRATANDO VÁRIOS VALORESv2.0
cont = soma = 0
numb = int(input('digite o numero: '))
menor = maior = numb
resp = 'S'
while resp != 'N':
    if numb > maior:
        maior = numb
    if numb < menor:
        menor = numb
    cont += 1
    soma = numb + soma
    resp = str(input('quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'S':
        numb = int(input('digite o numero: '))
med = soma / cont
print(f'voce digitou {cont} numeros e a média entre eles é {med:.2f}')
print(f'o maior número é {maior} e o menor número é {menor}')