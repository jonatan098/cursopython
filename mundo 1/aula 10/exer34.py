salar = float(input('qual o salario do funcionario? R$'))
if salar >=   1250.00:
    novo = salar + (salar * 10 / 100)
else:
    novo = salar + (salar * 15 / 100)
print(f'quem ganhava R${salar:.2F} agora ganha R${novo:.2F}')