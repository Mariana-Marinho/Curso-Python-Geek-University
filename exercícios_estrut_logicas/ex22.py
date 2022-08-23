"""
Calcular raízes de equação do 2º grau
"""


def baskhara(a, b, c):
    d = (b**2) - (4*a*c)
    if d < 0:
        return f'não há raiz real'
    elif d == 0:
        # raiz única
        x = (-b) / (2*a)
        return f'{x:.2f}'
    else:
        # duas raízes reais
        x1 = (-b + d**(1/2)) / (2*a)
        x2 = (-b - d**(1/2)) / (2*a)
        return f'{x1:.2f} e {x2:.2f}'


print('sendo uma equação do 2º grau da forma ax²+bx+c=0, informe:')
a = float(input('o valor de a: '))
b = float(input('o valor de b: '))
c = float(input('o valor de c: '))
print()
raiz = baskhara(a, b, c)
print(f'as raízes da equação {a}x²{f"+{b}" if b >= 0 else b}x{f"+{c}" if c >= 0 else c}=0 são: {raiz}')
