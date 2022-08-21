"""
Usando switch, programa que lê inteiro entre 1 e 7 e imprimir o dia da semana correspondente ao número
"""


def dia(numero):
    dias = {
        1: "domingo",
        2: "segunda",
        3: "terça",
        4: "quarta",
        5: "quinta",
        6: "sexta",
        7: "sábado"
    }
    # a função get retorna o value de acordo com o key informado
    return dias.get(numero)


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = int(numero)
            if numero not in range(1, 8):
                print(f'\033[31mdigite um número no intervalo\033[m')
                continue
        except:
            print(f'\033[31mdigite um número inteiro\033[m')
        else:
            return numero


num = ler_numero_positivo('digite um número entre 1 e 7: ')
print(f'o dia que você escolheu foi: {dia(num)}')
