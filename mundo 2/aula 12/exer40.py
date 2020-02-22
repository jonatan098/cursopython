nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'tirando {nota1:.1f} e {nota2:.1f}, a media é {media:.1f}')
if media < 5.0:
    print('o aluno esta REPROVADO')
elif 7 > media >= 5.0:
    print('o aluno esta RECUPERAÇÃO')
elif media >= 7:
    print('o aluno esta APROVADO')