"""
O maior palíndromo feito a partir de dois números de 3 dígitos
"""


def ler_palindrome(numero):
    numero = str(numero)
    i = 0
    j = len(numero) - 1
    while i <= j:
        if numero[i] != numero[j]:
            return False
        i += 1
        j -= 1
    return True


palindromo = 0
for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        palindromo = a*b
        if ler_palindrome(palindromo):
            print(f'o maior palíndromo possível é {palindromo} = {a} * {b}')
            exit()
