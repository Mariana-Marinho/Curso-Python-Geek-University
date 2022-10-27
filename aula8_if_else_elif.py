"""
Estrutura condicional:
    if:
        condição
    elif:
        (else if), condição após um if
        pode usar mais de uma vez
    else:
        o resto
"""
idade = int(input('digite sua idade: '))
if idade > 18:
    print('você é maior de idade')
elif idade == 18:
    print('você tem 18 anos')
else:
    print('você é menor de idade')
