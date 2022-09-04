"""
Calcular sequência fibonacci até o primeiro número superior ao lido
"""
limite = int(input('limite: '))
a = 1
b = 0
print('0...1...', end='')
while True:
    fibonacci = a + b
    b = a
    a = fibonacci
    print(fibonacci, end='...')
    if fibonacci > limite:
        break
