"""
Ler 10 números e escrever o maior, o menor e media usando lógica
"""
menor = maior = media = 0
numeros = []
for c in range(0, 10):
    digitado = float(input('digite um número: '))
    numeros.append(digitado)
    if c == 0 or digitado > maior:
        maior = digitado
    if c == 0 or digitado < menor:
        menor = digitado
    media += digitado
media /= 10
print(f'''
1- o maior número é {maior}
2- o menor é {menor}
3- a média é {media}''')
