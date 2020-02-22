def area():
    a = larg * comp
    print(f'a area de um terreno {larg}x{comp} é de {a:.1f}m².')


print('  controle de terrenos')
print('-='*15)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area()