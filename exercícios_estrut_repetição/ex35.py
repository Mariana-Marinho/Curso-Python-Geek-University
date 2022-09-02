"""
Programa que lê um número inteiro e informa se é primo ou não
"""
numero = int(input('digite um número inteiro: '))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f'o número não é primo pois é divisível por {i}')
            break
        elif i == numero-1:
            print(f'{numero} é primo!')

else:
    print(f'{numero} não é primo')


def primos(intervalo):
    lista_primos = []
    for num in range(2, intervalo+1):
        falso = 0
        for i in range(2, num):
            if num % i == 0:
                falso = 1
        if falso == 0:
            lista_primos.append(num)
    return lista_primos


print(primos(20))