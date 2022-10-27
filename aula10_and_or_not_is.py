"""
Estruturas lógicas:
    Operadores unários:
        not:
            o valor do booleano é invertido (True vira False; False vira True)

    Operadores binários:
        and:
            ambos precisam ser True
        or:
            um ou outro precisa ser True
        is:
            precisam ser iguais; compara com o segundo
"""
ativo = True
logado = True
# se ambos forem verdadeiros
if ativo and logado:
    print('Bem Vindo, usuário!')
else:
    print('Você precisa ativar sua conta.')
if not ativo:
    print('Você precisa estar ativo.')
elif ativo is logado:
    print('Você está logado e ativo')
