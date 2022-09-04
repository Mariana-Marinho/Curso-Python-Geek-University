"""
Somar os termos pares da sequência fibonacci cujos valores não ultrapassem 4 milhões
"""
a = 1
b = 0
soma = 0
while True:
    fibonacci = a + b
    b = a
    a = fibonacci
    if fibonacci >= 4_000_000:
        break
    if fibonacci % 2 == 0:
        print(fibonacci, end='...')
        soma += fibonacci
print(f'\na soma dos valores pares da sequência fibonacci vale {soma}')
