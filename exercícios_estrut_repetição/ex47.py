"""
Calcular alguma das 4 operações matemáticas
"""
while True:
    print(f"""{'MENU':^15}
[1]- somar
[2]- subtrair
[3]- multiplicar
[4]- dividir
[5]- sair""")
    escolha = int(input('sua escolha: '))
    if escolha == 1:
        print('a + b = resultado')
        a = float(input('a: '))
        b = float(input('b: '))
        print(f'{a} + {b} = {a+b}\n')
    elif escolha == 2:
        print('a - b = resultado')
        a = float(input('a: '))
        b = float(input('b: '))
        print(f'{a} - {b} = {a-b}\n')
    elif escolha == 3:
        print('a * b = resultado')
        a = float(input('a: '))
        b = float(input('b: '))
        print(f'{a} * {b} = {a*b}\n')
    elif escolha == 4:
        print('a / b = resultado')
        a = float(input('a: '))
        b = float(input('b: '))
        print(f'{a} / {b} = {a/b}\n')
    elif escolha == 5:
        print('PROGRAMA FINALIZADO')
    else:
        print('digite um número válido\n')
