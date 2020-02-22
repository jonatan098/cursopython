frase = str(input('digite uma frase: ')).strip().lower()
print('a letra \033[4;33;0mA\033[m aparece {} vezes'.format(frase.count('a')))
print('a primeira vez que ela aparece é na posição {}'.format(frase.find('a') + 1))
print('a ultima vez que ela aparece é na posição {}'.format(frase.rfind('a')+1))