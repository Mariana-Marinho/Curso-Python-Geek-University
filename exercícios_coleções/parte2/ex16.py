"""
Corrigir uma prova c 10 questões, sala com 3 alunos
ler o gabarito e a matrícula do aluno
printar a matrícula, respostas e nota, se foi aprovado ou não (>=7)
"""

respostas = []
resposta_aluno = []

gabarito = []
nota = 0

for i in range(3):
    resposta_aluno.append(int(input(f'\ndigite a matrícula do {i+1} aluno: ')))
    for j in range(10):
        resposta_aluno.append(input(f'resposta da {j+1} questão: '))
    respostas.append(resposta_aluno)
    resposta_aluno = []

print()
for i in range(10):
    gabarito.append(input(f'digite o gabarito da {i+1}ª questão:  '))

for i in range(3):
    print(f'\no {i+1}º aluno de matrícula {respostas[i][0]} tirou ', end='')
    for j in range(1, 11):
        if gabarito[j-1] == respostas[i][j]:
            nota += 1
    print(f'{nota}', end=' ')
    if nota >= 7:
        print('e ele foi aprovado')
    else:
        print('e ele foi reprovado')
    print(f'suas respostam foram: {respostas[i][1:]}')
    nota = 0

