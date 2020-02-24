# uma PA personalizada
from time import sleep
def contador(p1,pn,r):
    if r < 0:
        r *= -1
    if r == 0:
        r = 1
    print('-='*20)
    print(f'contagem de {p1} até {pn} de {r} em {r}')
    sleep(2.5)
    if p1 < pn:
        cont = p1
        while cont <= pn:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += r
        print('FIM!')
    else:
        cont = p1
        while cont >= pn:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= r
        print('FIM!')

#codigo principal
contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('agora e sua vez de persosonaliza a contagem.')
ini = int(input('INICIO: '))
end = int(input('FIM:    '))
pas = int(input('PASSO:  '))
contador(ini,end,pas)