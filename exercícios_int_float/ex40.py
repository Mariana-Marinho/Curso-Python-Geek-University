# solicitar o numero de dias trabalhados, sabendo que a diária vale 30,00 e imprimir o líquido, descontando 8%
dias = int(input('informe a quantidade de dias trabalhados: '))
valor_bruto = dias*30
valor_liq = valor_bruto*0.92
print(f'o salário bruto vale {valor_bruto:.2f}, contudo há o desconto de 8% do imposto de renda, '
      f'totalizando {valor_liq:.2f}')
