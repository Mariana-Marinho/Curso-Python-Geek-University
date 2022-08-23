"""
Calcular o valor a ser pago num lanche
"""

tabela = {
        100: 1.2,
        101: 1.3,
        102: 1.5,
        103: 1.2,
        104: 1.7,
        105: 2.2,
        106: 1}

pagar = 0
while True:
    print(''' 
    MENU
    
   Cachorro Quente - 100
   Bauru Simples - 101
   Bauru com Ovo - 102
   Hamburguer - 103
   Cheeseburguer - 104
   Suco - 105
   Refrigerante - 106
    ''')
    lanche = int(input('digite o código do lanche você quer comer: '))
    quant = int(input('quanto lanches?'))
    pagar += tabela.get(lanche)*quant
    e = input('vai querer mais alguma coisa? ')[0]
    if e in 'Nn':
        break
print(f'você pagará no total {pagar} reais')
