"""
Calcular o menor número divisível para cada um dos números de 1 a 20
"""
primos_lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                367, 373, 379]


def ler_mmc(a, b, primos):
    mmc = 1
    i = 0
    while True:
        if a % primos[i] == 0 or b % primos[i] == 0:
            mmc *= primos[i]
            if a % primos[i] == 0:
                a = a // primos[i]
            if b % primos[i] == 0:
                b = b // primos[i]
        else:
            i += 1
        if a == b == 1:
            return mmc


multiplo = 1
for numero1 in range(1, 21):
    multiplo = ler_mmc(numero1, multiplo, primos_lista)
print(multiplo)
