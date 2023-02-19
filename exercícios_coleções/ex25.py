"""
Preencher um vetor de tamanho 7 com os 100 primeiros naturais que não são multiplos de 7 ou terminam em 7
"""
naturais = []
num = 1
resto = 0

while len(naturais) != 100:
    if num % 7 != 0:
        naturais.append(num)
    else:
        resto = num
        while resto > 10:
            resto = resto // 10
        if resto == 7:
            naturais.append(num)
    num += 1

print(naturais)
