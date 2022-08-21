"""
Ler o salário e o valor da prestação de um empréstimo, não pode ser >20%salario
"""


def leia_numero(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


salario = leia_numero('digite o salário do funcionário: ')
prestacao = leia_numero('digite o valor da prestação do empréstimo: ')
if prestacao > 0.2*salario:
    print('empréstimo não concedido.')
else:
    print('empréstimo concedido.')
