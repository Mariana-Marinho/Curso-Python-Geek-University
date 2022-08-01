# programa que receba a altura e sexo de alguém e mostrar seu peso ideal conforme IMC
altura = float(input('digite sua altura em cm: '))
sexo = input('seu sexo é feminino ou masculino? ')
if sexo.upper().find("MASCULINO") != -1:
    imc = (0.727*altura)-58
    print(f'seu peso ideal equivale a {imc:.2f}kg')
elif sexo.upper().find("FEMININO"):
    imc = (0.621*altura)-44.7
    print(f'seu peso ideal é {imc:.2f}kg')
else:
    print('digite corretamente.')
