#DESCOBRINDO A SOMA DOS IMPARES MULTIPLOS DE 3 DE 1 ATE 500
soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'a soma dos {cont} numeros solicitados é {soma} ')
