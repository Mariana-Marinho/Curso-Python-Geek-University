"""
Ler valores e mostrar o quadrado, cubo e raiz
"""
while True:
    num = float(input('número: '))
    if num <= 0:
        print('PROGRAMA FINALIZADO')
        break
    print(f'o quadrado de {num} é {num**2}')
    print(f'o cubo de {num} é {num**3}')
    print(f'a raiz de {num} é {num**(1/2):.2f}\n')
