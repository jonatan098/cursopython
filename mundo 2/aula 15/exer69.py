#ANALISE DE DADOS
cont18 = conth = contm20 =  0
while True:
    age = int(input('idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('sexo [M/F]: ')).upper().strip()[0]
    if sex == 'M':
        conth += 1
    if age < 20 and sex == 'F':
        contm20 += 1
    if age > 18:
        cont18 += 1
    next = ' '
    while next not in 'SN':
        next = str(input('quer continuar? [S/N]')).upper().strip()[0]
    if next == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {cont18}')
print(f'ao todo temos {conth} homens cadastrados')
print(f'e temos {contm20} mulheres com menos de 20 anos')