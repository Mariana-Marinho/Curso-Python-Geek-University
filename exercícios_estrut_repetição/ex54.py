"""
Ver se um número é primo
"""
numero = int(input('digite um número: '))
for i in range(2, numero):
    if numero % i == 0:
        print(f'o número {numero} não é primo')
        exit()
print(f'o número {numero} é primo')
