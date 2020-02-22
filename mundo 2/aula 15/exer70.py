#ESTATÍSTICAS EM PRODUTOS
tot = mais = menor = cont = 0
barato = ''
while True:
    namep = str(input('nome do produto: '))
    price = int(input('preço: R$'))
    cont += 1
    tot += price
    if price > 1000:
        mais += 1
    if cont == 1 or price < menor:
        menor = price
        barato = namep
    next = ' '
    while next not in 'SN':
        next = str(input('quer continuar? [S/N]')).upper().strip()[0]
    if next == 'N':
        break
print(f'o total de compra foi R${tot:.2f}')
print(f'temos {mais} produtos custando mais de R$1000.00')
print(f'o protudo mais barato foi {barato} que custo R${menor:.2f}')