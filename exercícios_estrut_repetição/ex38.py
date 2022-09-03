"""
Calcular termo pitagórico a, b, c para a+b+c=1000
"""
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000:
                break
            if a**2+b**2 == c**2 and a != b != c:
                print(f'{a}² + {b}² = {c}²')
