"""
Calcular termo pitagórico a, b, c para a+b+c=1000
"""
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a**2+b**2 == c**2 and a != b != c:
            print(f'{a}² + {b}² = {c}²')
