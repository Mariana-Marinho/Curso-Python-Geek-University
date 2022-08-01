# usando switch, programa que lê inteiro entre 1 e 7 e imprimir o dia da semana correspondente ao número
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
    return dias.get(numero, "não é um número válido")

num = int(input('digite um inteiro entre 1 e 7: '))
print(f'o dia que você escolheu foi: {dia(num)}')
