"""
Dicionários
    dict = {key1: value1, key2: value2}


Conjuntos
    set = {value1, value2, value3}

    sem key
    não tem ordem nem valores duplicados


Modulo Collections - Counter
    recebe um interavel como parametro e cria um objeto do tipo collections counter parecido com um dicionário, tendo chave e elemento da lista passada como parametro e como valor a quantidade de ocorrencias do elemento

    ficaria:
        from collections import Counter

        lista = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5]
        res = Counter(lista)
        print(type(res))
        print(res)
    vai printar:
        <class 'collections.Counter'>
        Counter({1: 5, 2: 4, 3: 2, 5: 1})


Modulo Collections - Default Dict
    ao criar um dict usando o Default Dict, informa-se um valor default,
        podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver valor definido. Sempre que
        tentarmos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

    lambda: funcao sem nome, que podem ou não receber parametro de entrado e devolver valores

    ficaria:
        from collections import defaultdict

        dict = defaultdict(lambda: 0)

        dict[nome] = 'mariana'

        print(dict)
        print(dict[outro])
        print(dict)
    vai printar:
    {'mariana'}
    0
    {'mariana', 0}


Modulo Collections - Ordered Dict
    estabelece uma ordem para o dicionário conforme a key


Modulo collections - namedtuple
    tuplas onde se especifica um nome e parâmetros

    ficaria:
        from collection import namedtuple

        cachorro = namedtuple('cachorro', 'idade raca nome') #ou namedtuple('cachorro', 'idade, raca, nome') #ou namedtuple('cachorro', ['idade raca nome'])
        lulu = cachorro(idade = 2, raca='chow-chow', nome='Lulu')

        print(lulu)
    vai printar:
        cahorro(idade=2, raca='chow-chow', nome='Lulu')


Modulo collections - Deque
    lista de alta performance

    ficaria:
        from collections import deque

        deq = deque('mariana')
        print(deq)

        deq.append('!!!')
        deq.appendleft('sou')
    vai printar:
        deque(['m', 'a', 'r', 'i', 'a', 'n', 'a'])
        deque(['m', 'a', 'r', 'i', 'a', 'n', 'a', '!!!'])
        deque(['sou', 'm', 'a', 'r', 'i', 'a', 'n', 'a', '!!!'])

"""