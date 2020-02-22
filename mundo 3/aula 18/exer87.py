matrix = [[0,0,0], [0,0,0], [0,0,0]]
somapar = somac3 = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'digite um numero [{l}][{c}]: '))
        if matrix[l][c] % 2 == 0:
            somapar += matrix[l][c]
        if c == 2:
            somac3 += matrix[l][c]
        if l == 1 and matrix[l][c] > maior:
            maior = matrix[l][c]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'a soma de todos os numeros pares foi: {somapar}')
print(f'a soma dos numeros da terceira coluna foi: {somac3}')
print(f'o maior numero da segunda linha foi: {maior}')