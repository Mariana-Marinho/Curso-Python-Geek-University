# ler os valores do cateto de um triângulo e calcular o valor da hipotenusa
from math import hypot
cat_1 = float(input('digite o valor do primeiro cateto: '))
cat_2 = float(input('digite o valor do segundo cateto: '))
hip = hypot(cat_1, cat_2)
print(f'a hipotenusa do triânculo cujos catetos são {cat_1} e {cat_2}, vale {hip}')
