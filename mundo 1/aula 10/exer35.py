print('-='*20)
print('ANALISADOR DE TRIÂNGILOS')
print('-='*20)
r1 = float(input('digite a primeira medida: '))
r2 = float(input('digite a segunda medida: '))
r3 = float(input('digite a terceira medida: '))
"""if r2-r3<r1<r2+r3:
    if r1-r3<r2<r1+r3:
        if r1-r2<r3<r1+r2:
            print(f'com {r1},{r2} e {r3} voce pode formar um triângulo!')
else:
    print(f'com {r1},{r2} e {r3} voce não pode formar um triângulo!')"""
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print(f'com {r1},{r2} e {r3} voce podem formar um triângulo')
else:
    print(f'com {r1},{r2} e {r3} voce não podem formar um triângulo')