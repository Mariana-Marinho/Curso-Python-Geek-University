# ler as dimensões de um terreno e o preço do metro de tela, imprimir o custo para cercar o terreno
largura = float(input('digite a largura do terreno: '))
comprimento = float(input('digite o comprimento do terreno: '))
preco = float(input('digite o preço do metro da cerca: '))
custo = largura*comprimento*preco
print(f'o custo para cercar o terreno será de {custo:.2f}')
