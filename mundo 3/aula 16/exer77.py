words = ('aprender','linguagem','programar','python','curso','gratis','praticar')
for p in words:
    print(f'\nna palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')