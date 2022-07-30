# ler um número inteiro e imprimir 1 dígito por linha
num = input('digite um número: ')
i = 0
print('dígitos por linhas:')
while i < len(num):
    print(f'{num[i]}')
    i += 1
