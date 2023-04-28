"""
Tuplas ()
    - Tuplas são coleções, assim como listas, mas são IMUTÁVEIS, não dá para mudar
    - Definidas pela vírgula, e não pelo uso dos parênteses
    - Mais rápidas nas operações do que listas

    ex.:
        podem ser declaradas com () ou sem
            tupla = (1, 2, 3)

            tupla = 1, 2, 3


        tuplas de tamanho 1:
            tupla = (4,)

            tupla = 4,

            int = (4)


    ex.:
        tupla = tuple(range(10))

        # desempacotamento nas tuplas:
        nome_completo = Mariana, Marinho
        primeiro_nome, sobrenome = nome_completo


    iterando sobre tupla:
        for indice, valor in enumerate(/tupla):
            print(indice, valor)

        tupla.count(argumento)
            conta quantos argumentos tem na tupla

        for elemento in tupla:
            print(elemento)


"""
