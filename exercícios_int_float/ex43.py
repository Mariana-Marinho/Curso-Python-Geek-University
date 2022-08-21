"""
Programa que lê uum valor e o mostre:
    com desconto de 10%;
    valor de cada parcela em 3x sem juros;
    comissão do vendedor, caso a venda seja à vista, 5% sobre o valor com desconto;
    comissão do vendedor, caso a venda parcelada, 5% sobre o total
"""
valor = float(input('digite o valor do produto: '))
desconto = valor*0.9
print(f""" Informações de pagamento acerca do produto de valor {valor}
1- o total a pagar será de  {desconto:.2f}
2- caso parcele em 3x, cada parcela custará {desconto/3:.2f}
3- caso a venda seja à vista, o vendedor receberá comissão de {0.05*desconto:.2f}
4- caso a venda seja parcelada, o vendedor receberá comissão de {0.05*valor:.2f}.
""")
