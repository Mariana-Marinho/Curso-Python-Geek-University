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
    return meses.get(numero, " ERROR não é um número válido")


num = int(input('digite um inteiro entre 1 e 12: '))
print(f'o mês escolhido foi {mes(num)}')
