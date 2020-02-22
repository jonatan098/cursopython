from datetime import datetime
dados = {}
dados['nome'] = str(input('nome: '))
ano = int(input('data de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('carteira de trabalho (0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('sálario: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')