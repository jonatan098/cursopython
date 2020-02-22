main = [[],[]]
numb = 0
for v in range(1,8):
    numb = int(input(f'digite {v}º valor: '))
    if numb%2 == 0:
        main[0].append(numb)
    else:
        main[1].append(numb)
main[0].sort()
main[1].sort()
print(f'os valores pares digitados foram: {main[0]}')
print(f'os valores impares digitados foram: {main[1]}')