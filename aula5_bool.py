"""
Tipo bool

2 constantes:
    True
    False

    OBR: 1a LETRA MAIÚSCULA!!!

"""

ativo = True
print(ativo, 'ativo')
print(not ativo, 'not ativo')

logado = False
print(False, 'logado')
print(ativo or logado, 'ativo or logado')

respondeu = False
print(respondeu, 'respondeu')
print(logado or respondeu, 'logado or respondeu')


"""
Operações básicas:
    Not:
        fazendo a negação, se o valor booleano for True, o resultado será False e vice versa   

    Or:
        operação binária, precisa de dois valores; um dos dois deve ser True
            True:
                True or False
                False or True
                True or True
            
            False:
                False or False

    And:
        operação binária, ambos valores devem ser verdadeiros
            True:
                True and True
            
            False:
                False and True
                True and False
                False and False

"""
