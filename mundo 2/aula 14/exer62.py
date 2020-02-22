#PROGRESSÃO ARITMÉTICA(PA)3.0
p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
pa = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(pa,end=' -> ')
        pa += r
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos a mais voce quer? '))
print(f'PA finalizada com {total} termos.')

