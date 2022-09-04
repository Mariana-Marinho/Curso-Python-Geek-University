"""
Ler idades e calcular a média
"""
pessoa = 1
idades = []
while True:
    pessoa = int(input('anos: '))
    if pessoa <= 0:
        break
    idades.append(pessoa)
media = sum(idades)/len(idades)
print(f'a média das idades informadas foi {media}')
