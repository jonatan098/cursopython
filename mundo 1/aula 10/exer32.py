ano = int(input('digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} e um ano bissexto'.format(ano))
else:
    print('{} não e um ano bissexto'.format(ano))