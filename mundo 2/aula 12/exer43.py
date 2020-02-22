peso = float(input('digite o seu peso(kg): '))
altura = float(input('digite sua altura(m): '))
IMC = peso / altura ** 2
print(f'o IMC dessa pessoa é de {IMC:.1f}')
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= IMC < 25:
    print('PESO IDEAL')
elif 25 <= IMC < 30:
    print('SOBREPESO')
elif 30 <= IMC < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
