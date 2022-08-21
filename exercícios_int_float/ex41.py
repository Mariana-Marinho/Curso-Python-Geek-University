# programa que lê o valor da hora de trabalho e horas trabalhadas no mês, com 10% de acréscimo
valor = float(input('insira o valor da hora trabalhada: '))
horas = float(input('insira a quantidade de horas trabalhadas: '))
salario = valor*horas*1.1
print(f'o salário do funcionário será R${salario:.2f}')
