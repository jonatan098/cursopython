#PROGRESSÃO ARITMÉTICA(PA)
p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
n = p1 + (10-1) * r
for c in range(p1,n+r,r):
    print(c)