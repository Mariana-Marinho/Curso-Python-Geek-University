"""
Ler a matriz 5x4 com:
primeira coluna: numero de matrícula
segunda coluna: média das provas
terceira coluna: média dos trabalhos
quarta coluna: nota final (soma das médias)

Ler a 1, 2 e 3 coluna
matricula do aluno com maior nota
media das notas finais
"""

alunos = []
informacao_aluno = []

notas_finais = 0

for i in range(5):
    for j in range(4):

        if j == 0:
            informacao_aluno.append(int(input(f'\nmatricula do {i+1} aluno: ')))

        elif j == 1:
            informacao_aluno.append(float(input(f'media das provas: ')))

        elif j == 2:
            informacao_aluno.append(float(input(f'media dos trabalhos: ')))

        else:
            nota_final = (informacao_aluno[1] + informacao_aluno[2])
            informacao_aluno.append(nota_final)

    alunos.append(informacao_aluno)
    informacao_aluno = []

maior_nota = alunos[0][3]
aluno_maior_nota = alunos[0][0]

for i in range(5):
    notas_finais += alunos[i][3]
    if alunos[i][3] > maior_nota:
        maior_nota = alunos[i][3]
        aluno_maior_nota = alunos[i][0]

print(f'\no aluno que obteve a maior nota ({maior_nota}) foi o de matrícula {aluno_maior_nota}')
print(f'a media das notas finais foi {notas_finais/5}')
