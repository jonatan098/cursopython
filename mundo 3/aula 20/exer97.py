#mostre uma menssagem com tamanho adaptavel
def escreva(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
#codigo principal
quant = int(input('quantas palavras vai querer escrever: '))
for p in range(0,quant):
    word = str(input('escreva uma palavra: '))
    escreva(word)

