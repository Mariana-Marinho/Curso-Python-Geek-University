"""
Receber dois vetores A e B com 10 inteiros cada
criar vetor C com C = A - B
"""

A = []
B = []
C = []

for i in range(10):
    A.append(int(input('digite um valor para o vetor A: ')))

print()

for i in range(10):
    B.append(int(input('digite um valor para o vetor B: ')))

for i in range(10):
    num = A[i] - B[i]
    C.append(num)

print(f'a lista C ficou {C}')
