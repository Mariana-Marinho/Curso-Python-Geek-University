"""
Desenhar uma linha na tela
"""


def draw_line(quant):
    for i in range(quant):
        print('-', end='')


x = int(input('digite a quantidade de traços na linha: '))
draw_line(x)
