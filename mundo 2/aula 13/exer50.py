#CALCULANDO A SOMA DOS NUMEROS PARES
soma = 0
cont = 0
for c in range(1,7):
    numb = int(input(f'digite {c}° numero: '))
    if numb % 2 == 0:
        cont += 1
        soma += numb
print(f'voce digitou {cont} numeros pares e a soma deles é {soma}')