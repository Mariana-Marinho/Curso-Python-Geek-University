"""
Calcular o IMC de uma pessoa e mostrar sua situação
"""
peso = float(input('peso em kg: '))
altura = float(input('altura em m: '))
imc = peso / altura**2
print('você esta', end='')
if imc < 18.6:
    print('abaixo do peso')
elif 18.6 <= imc < 25:
    print('saudável')
elif 25 <= imc < 30:
    print('peso em excesso')
elif 30 <= imc < 35:
    print('obesidade grau 1')
elif 35 <= imc < 40:
    print('obesidade grau 2')
else:
    print('obesidade grau 3')
