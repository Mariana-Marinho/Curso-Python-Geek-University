# usando switch, ler um inteiro entre 1 e 12 e imprimir o mês correspondente
def mes(numero):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    return meses.get(numero)


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = int(numero)
            if numero not in range(1, 13):
                print(f'\033[31mdigite um número no intervalo\033[m')
                continue
        except:
            print(f'\033[31mdigite um número inteiro\033[m')
        else:
            return numero


num = ler_numero_positivo('digite um número entre 1 e 12: ')
print(f'o mês escolhido foi {mes(num)}')
