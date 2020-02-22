from datetime import date
atual = date.today().year
ano = int(input('digite o seu ano de nascimento: '))
idade = atual - ano
print(f'o atleta tem {idade}')
if idade <= 9:
    print('sua categoria é MIRIN')
elif idade <= 14:
    print('sua categoria é INFANTIL')
elif idade <= 19:
    print('sua categoria é JUNIOR')
elif idade <= 25:
    print('sua categoria é SÉNIOR')
else:
    print('sua categoria é MASTER')