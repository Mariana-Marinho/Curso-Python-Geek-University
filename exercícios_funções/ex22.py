"""
Gerar n linhas com n exclamações
"""


def print_line(number):
    for i in range(1, number+1):
        print(f'{"!"*i}')


x = int(input('quantas linhas: '))
print_line(x)