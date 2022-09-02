"""
Ler dois números e imprimir os primeiros n números múltiplos de ambos
"""
multiplos = int(input('digite quantos números deseja: '))
primeiro = int(input('qual o primeiro número? '))
segundo = int(input('qual o segundo número? '))
num = 0
contador = 0
print(f'os {multiplos} múltiplos de {primeiro} e {segundo} são: ', end='')
while contador < multiplos:
    if num % primeiro == 0 or num % segundo == 0:
        print(f'{num}', end='...')
        contador += 1
    num += 1
