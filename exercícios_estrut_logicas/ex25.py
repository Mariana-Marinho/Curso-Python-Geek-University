"""
Ler 3 int e calcular valores de acordo com o menu
"""


def geometrica(x, y, z):
    media = (x*y*z)**(1/3)
    return media


def ponderada(x, y, z):
    media = (x + 2*y + 3*z)/6
    return media


def harmonica(x, y, z):
    media = 1 / ((1/x) + (1/y) + (1/z))
    return media


def aritmetica(x, y, z):
    media = (x+y+z) / 3
    return media


print("""MENU
1 - média geométrica
2 - média ponderada
3 - média harmônica
4 - média aritmética
""")
escolha = int(input('sua escolha: '))
x = float(input('digite x: '))
y = float(input('digite y: '))
z = float(input('digite z: '))
print()
if escolha == 1:
    media = geometrica(x, y, z)
    print(media)
elif escolha == 2:
    media = ponderada(x, y, z)
    print(media)
elif escolha == 3:
    media = harmonica(x, y, z)
    print(media)
elif escolha == 4:
    media = aritmetica(x, y, z)
    print(media)
else:
    print('valor não válido')
