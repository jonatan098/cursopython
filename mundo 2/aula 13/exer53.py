#DETECTOR DE POLÍNDROMO
frase = str(input('digite uma frase: ')).strip().upper()
words = frase.split()
junto = ''.join(words)
inver = ''
for letra in range(len(junto)-1,-1,-1):
    inver += junto[letra]
print(f'o inverso de {junto} é {inver}')
if junto == inver:
    print('logo é um polindromo!!!')
else:
    print('logo NÃO é um polindromo!!!')

