"""
Matriz 10x3 com notas de 10 alunos em 3 provas
quantos alunos tiveram a pior nota na 1a prova, na 2a e na 3a
"""

notas = []
aluno = []

primeira = segunda = terceira = 0

for i in range(10):
    for j in range(3):
        aluno.append(int(input(f'digite a nota da {j+1} prova do {i+1} aluno: ')))
    notas.append(aluno)
    aluno = []

for i in range(10):
    menor = min(notas[i])
    if notas[i].index(menor) == 0:
        primeira += 1
    elif notas[i].index(menor) == 1:
        segunda += 1
    elif notas[i].index(menor) == 2:
        terceira += 1

print(f'\n{primeira} alunos tiraram a pior nota na primeira prova')
print(f'{segunda} alunos tiraram a pior nota na segunda prova')
print(f'{terceira} alunos tiraram a pior nota na segunda prova')
