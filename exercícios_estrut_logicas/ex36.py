"""
Número de dígitos de um número inteiro positivo
"""
digitos = 0
num = input('numero: ').replace(' ', '').split()
for i in range(len(num)):
    if num[0] == 0:
        del num[0]
    else:
        break
# unindo a lista num inteiro
numero = int(''.join(num))
for i in range(len(num)):
    numero = numero % 10
    digitos += 1
print(f'o {num[0]} tem {digitos} dígitos válidos')
