casa = float(input('valor da casa: R$'))
salario = float(input('salario da comprador: R$'))
anos = int(input('quandos anos de finaciamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R${casa:.2f} em {anos} anos a prestação sera de R${prestação:.2f}')
if prestação <= minimo:
    print('o emprestimo pode ser concedido')
else:
    print('emprestimo negado')