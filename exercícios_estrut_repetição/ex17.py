"""
Ler um inteiro n e calcular a soma dos n primeiros números naturais
"""
soma = 0
numero = int(input('digite um inteiro positivo: '))
for i in range(0, numero+1):
    soma += i
print(f'a soma dos {numero} números naturais deu {soma}')
