#REGISTRANDO SEXO
sex = str(input('qual seu sexo [M/F]: ')).upper().strip()[0]
#while sex not in 'MnFf':
while sex != 'M' and sex != 'F':
    sex = str(input('dados incorretos. digite de novo, qual o seu sexo [M/F]: ')).upper().strip()[0]
print(f'sexo {sex} registrado com sucesso')