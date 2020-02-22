valores = []
maior = menor = 0
for v in (range(0,5)):
    valores.append(int(input(f'digite um numero para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:   
        if valores[v] >= maior:
            maior = valores[v]
        if valores[v] <= menor:
            menor = valores[v]   
print(f'voce digitou os valores {valores}')
print(f'o maior valor digitado foi {maior} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}....', end='')
print()
print(f'o menor valor digitado foi {menor} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}....', end='')
print()