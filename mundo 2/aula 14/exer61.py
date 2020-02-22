#PROGRESSÃO ARITMÉTICA(PA)2.0
p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
pa = p1
cont = 1
while cont <= 10:
    print(pa,end=' -> ')
    pa += r
    cont += 1
print('FIM')