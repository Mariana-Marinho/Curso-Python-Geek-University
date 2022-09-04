"""
João recebe 1/3 do salário de Carlos
Carlos aplica seu salário e rende 2% ao mês
João aplica seu salário e rende 5% ao mês
imprimir quantos meses para que o valor de joão ultrapasse ou iguale ao de carlos
"""
carlos = float(input('digite o salário de carlos: '))
joao = carlos/3
print(f'joao recebe {joao}')
meses = 0
while True:
    joao += joao*1.05
    carlos += carlos*1.02
    meses += 1
    if joao >= carlos:
        print(f'foram {meses} meses para João ultrapassar Carlos')
        break
