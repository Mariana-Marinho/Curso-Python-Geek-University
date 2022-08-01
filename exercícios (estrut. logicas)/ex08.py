# ler o salário e o valor da prestação de um empréstimo, não pode ser >20%salario
salaio = float(input('digite o salário do funcionário: '))
prestacao = float(input('digite o valor da prestação do empréstimo: '))
if prestacao > 0.2*salaio:
    print('empréstimo não concedido.')
else:
    print('empréstimo concedido.')
