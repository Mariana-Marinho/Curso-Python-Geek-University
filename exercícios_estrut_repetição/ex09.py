"""
Ler um inteiro n e ler os n primeiros números naturais ímpares
"""
digitado = int(input('digite um número: '))
limite = digitado*2+2
print(f'os {digitado} primeiros pares são: ', end='')
for c in range(2, limite, 2):
    print(c, end='...')
