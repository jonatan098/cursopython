# Faça um programa que 
# tenha uma função chamada área() 
# que receba as dimensões de uma terreno retangular (largura e comprimento)
# e mostre a área do terreno

def título():
    text = "Controle de terrenos"
    print(text)
    print("-" * len(text))

def area():
    a = larg * comp
    print(f'a area de um terreno {larg}x{comp} é de {a:.1f}m².')


print('  controle de terrenos')
print('-='*15)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
título()
area()
