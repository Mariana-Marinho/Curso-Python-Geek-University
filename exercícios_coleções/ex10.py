"""
Ler nota de 15 alunos e calcular média
"""

notas = []
for i in range(0, 15):
    aluno = float(input(f'digite a nota do {i+1}º aluno: '))
    notas.append(aluno)
media = sum(notas)/len(notas)
print(f'a média das notas foi {media}')
