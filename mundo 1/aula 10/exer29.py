velo = float(input('qual e a velocidade do carro? '))
if velo > 80:
    print(f'\033[7;31;0mvoce foi multado em R${(velo-80)*7:.2f}\033[m')
else:
    print('voce esta na velocidade permitida')
print('\033[1;33;0mtenha um bom dia!')