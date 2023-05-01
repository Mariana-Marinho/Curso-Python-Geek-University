"""
Tres notas e uma letra, media das notas ou media ponderada
"""


def get_score(x, y, z, type):
    """
    Recebe 3 notas e retorna média ponderada ou aritmética
    :param x: nota 1
    :param y: nota 2
    :param z: nota 3
    :param type: letra informando se a méria será ponderada ou aritmética
    :return: média
    """
    if type == 'p':
        media = (x*5 + y*3 + z*2)/10
    else:
        media = (x+y+z)/3
    return media


a, b, c = (float(i) for i in (input('digite as três notas do aluno: '). split()))
m = input('digite P para média ponderada e A para média aritmética: ').lower()
print(f'a média', 'aritmética' if m == 'a' else 'ponderada', f'das notas {a},{b} e {c} vale {get_score(a, b, c, m)}')
