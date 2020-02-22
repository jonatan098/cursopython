expres = str(input('digite uma expressão: '))
p = []
for s in expres:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('expressão valida!!')
else:
    print('expressão invalida!!')