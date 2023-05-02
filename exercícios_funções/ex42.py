"""
Vetor de reais e retorna a media deles
"""


def get_media(lista):
    soma = 0
    for i in lista:
        soma += float(i)
    media = soma / len(lista)
    return media


LISTA = input('digite alguns valores: ').split()
print(f'a media dos valores é {get_media(LISTA)}')
