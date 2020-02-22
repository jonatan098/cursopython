# Faça um programa que 
# tenha uma função chamada área() 
# que receba as dimensões de uma terreno retangular (largura e comprimento)
# e mostre a área do terreno

def área(largura, comprimento):
    return largura * comprimento

def título():
    text = "Controle de terrenos"
    print(text)
    print("-" * len(text))

def main():
    largura = float(input("LARGURA (m): "))
    comprimento = float(input("COMPRIMENTO (m): "))
    area = área(largura, comprimento)

    título()
    print(f'A área de um terreno {largura} X {comprimento} é {area}m²')

main()