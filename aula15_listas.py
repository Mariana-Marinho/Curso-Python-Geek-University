"""
Listas []
    - Funcionam com vetores/matrizes (arrays), mas são DINÂMICAS e podemos botar qualquer tipo de dados
    - Dinâmicas: não possui tamanho fixo, podemos criar a lista e ir adicionando elementos
    - Não possuem tipo fixo de dado, pode-se colocar qualquer dado

    ex.:
        lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
        lista2 = ['M',
        lista3 = []
        lista4 = ['M', 'A', 'R', 'I', 2, 0, 0, 2]

    - O comando list(conteúdo) faz uma lista do que você por dentro

    ex.:
        lista5 = list(range(11))    #vai virar uma lista com [0, 1, 2,..., 10]
        lista6 = list('Mari')    # vai virar uma lista ['M', 'a', 'r', 'i']

        if 'M' in lista6:
            print('a letra M está no nome')
        else:
            print('a letra M não está no nome')

    - Comandos para usar na lista:
        lista.sort() ou sorted(lista)
            vai ordenar em ordem crescente ou alfabética

        lista.count(elemento)
            vai contar quantas vezes o elemento apareceu na lista

        lista.append(elemento)
            vai adicionar o elemento ao final da lista

        lista.extend([elemento, elemento, ...])
            vai adicionar esses elementos ao final, não vai adicionar como sublista, vai adicionar individualmente

        lista.insert(index, elemento)
            vai enfiar um novo elemento nesse index indicado

        lista.reverse() ou lista[::-1]
            vai inverter a lista

        lista.copy()
            copia o valor de uma lista, porque se igualar elas vão estar ligadas

        len(lista)
            mostra quantos valores tem na lista

        lista.pop()
            remove o último elemento da lista, print(lista.pop()) retorna o elemento que removeu

        lista.pop(2)
            remove o elemento desse index

        lista.

    - Pode somar listas

        ex.:
            lista1 = [1, 2, 3]
            lista2 = [100, 200, 300]
            lista3 = lista1 + lista2    #lista3 vai ser [1, 2, 3, 100, 200, 300]
"""
lista6 = list('Mari')
if 'M' in lista6:
    print('a letra M está no nome')
    print(lista6)
else:
    print('a letra M não está no nome')
