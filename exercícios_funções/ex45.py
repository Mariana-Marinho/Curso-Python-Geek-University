"""
Desvio padrao
"""
def desvio_padrao(lista):
    media = sum(lista)/len(lista)
    soma = 0
    for i in lista:
        soma += (i - media)**2
    desvio = (soma / (len(lista)) - 1) ** (1/2)
    return desvio


LISTA = input('digite valores: ').split()
print(f'o desvio padrão da lista é {desvio_padrao(LISTA)}')
