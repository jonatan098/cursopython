print('-='*20)
print('ANALISADOR DE TRIÂNGILOS')
print('-='*20)
r1 = float(input('digite a primeira medida: '))
r2 = float(input('digite a segunda medida: '))
r3 = float(input('digite a terceira medida: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('as medidas podem formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    elif r1 != r2 != r3:
        print('ISÓSCELES')
else:
    print(f'com {r1},{r2} e {r3} voce não podem formar um triângulo')