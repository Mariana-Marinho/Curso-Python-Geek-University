# ler quatro notas e calcular a média
a, b, c, d = input('digite quatro notas dos alunos: ').split()
media = (float(a)+float(b)+float(c)+float(d))/4
print(f'a média das notas {a, b, c, d} é: {media}')
if media >= 7:
    print(f'\033[34;4mVOCÊ PASSOUUUUU')
else:
    print('vai ter que fazer recuperação.......')
