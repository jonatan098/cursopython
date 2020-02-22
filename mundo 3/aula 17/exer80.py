valores = []
for p, c in enumerate(range(0,5)):
    num = int(input('digite um numero: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print(f'{num} foi adicionado na ultima posição...')
    else:
        pos = 0
        while pos <= len(valores):
            if num <= valores[pos]:
                valores.insert(pos,num)
                print(f'{num} foi adicinado na posição {p}...')
                break
            pos += 1
print(f'os numeros digitados em ordem foram: {valores}')