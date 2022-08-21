"""
Calcular valor do produto com diferentes taxas de imposto por estado
"""

def taxa(estado):
    impostos = {
        'MG': 0.07,
        'SP': 0.12,
        'RJ': 0.15,
        'MS': 0.08
    }
    return impostos.get(estado)


preco = float(input('digite o valor do produto: '))
while True:
    uf = input('digite a UF do estado que deseja: ').upper().strip()
    try:
        imposto = taxa(uf)
    except:
        print('digite uma uf válida')
    else:
        break
print(f'o valor final em {uf} ficará {preco*(1+imposto):.2f}')
