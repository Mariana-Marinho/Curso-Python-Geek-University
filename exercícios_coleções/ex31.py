"""
Ler dois vetores e criar um com a uniao dos dois
"""
primeiro = []
segundo = []
uniao = []

for i in range(10):
    primeiro.append(int(input('digite um valor: ')))

for i in range(10):
    segundo.append(int(input('digite um valor: ')))

for num in primeiro:
    if num not in uniao:
        uniao.append(num)

for num in segundo:
    if num not in uniao:
        uniao.append(num)

print(f'a união é {uniao}')
