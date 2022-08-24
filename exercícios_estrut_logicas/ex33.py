"""
Calcular o aumento do salário, inversamente proporcional ao valor
"""
salario = float(input('digite seu salário: '))
tempo = float(input('há quantos anos você atua na empresa? '))
if salario < 500:
    salario *= 1.25
elif salario < 1000:
    salario *= 1.2
elif salario < 1500:
    salario *= 1.15
elif salario <= 2000:
    salario *= 1.1
if 1 <= tempo <= 3:
    salario += 100
elif tempo <= 6:
    salario += 200
elif tempo <= 10:
    salario += 300
else:
    salario += 500
print(f'seu salário foi reajustado a {salario}')
