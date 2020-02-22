#SEQUÊNCIA DE FIBONACCI
numb = int(input('quantos numeros voce quer importar? '))
c = 3
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),end=' -> ')
while c <= numb:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')