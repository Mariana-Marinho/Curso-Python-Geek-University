"""
5 primeiros múltiplos de 3
"""
c = 1
d = 0
print(f'os 3 primeiros múltiplos de 3 são: ', end='')
while d < 3:
    if c % 3 == 0:
        d += 1
        print(c, end='...')
    c += 1