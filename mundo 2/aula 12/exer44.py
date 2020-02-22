preço = float(input('qual o valor do produto R$'))
print('''escolha a condição de pagamento:
 [1]a vista dinheiro/cheque
 [2]a vista cartão
 [3]2x no cartão
 [4]3x ou mais''')
cond = int(input('qual é a opção? '))
if cond == 1:
    print(f'sua compra de R${preço:.2f} vai custar R${preço - (10 * preço / 100):.2f} no final')
elif cond == 2:
    print(f'sua compra de R${preço:.2f} vai custar R${preço - (5 * preço / 100):.2f} no final')
elif cond == 3:
    print(f'sua compra sera parcelada em 2x R${preço / 2:.2f}')
    print(f'sua compra vai custar R${preço:.2f} no final')
elif cond == 4:
    parce = (input('quantas parcelas? '))
    print(f'sua compra será parcelada em {parce}x de R${preço} COM JUROS')
    print(f'sua compra de R${preço:.2f} vai custar R${preço + (preço * 20 / 100):.2f} no final')
