"""
Ler matriz 5x10 de respostas e uma lista de 10 indices com o gabarito, fazer as notas
"""

respostas = []
resposta_aluno = []

gabarito = []

nota_aluno = 0

for i in range(5):
    print(f'\n aluno {i+1}')
    for j in range(10):
        resposta_aluno.append(input(f'{j+1} questao: '))
    respostas.append(resposta_aluno)
    resposta_aluno = []

for n in range(10):
    gabarito.append(input(f'gabarito da {n+1} questão: '))

for i in range(5):
    print(f'\n o {i+1} aluno acertou a(s) questão(ões): ', end='')
    for j in range(10):
        if gabarito[j] == respostas[i][j]:
            print(j, end='...')
            nota_aluno += 1
    print(f'\no {i+1} aluno tirou {nota_aluno}')
    nota_aluno = 0

print('\n as respostas foram: ')
for aluno in respostas:
    print(aluno)
