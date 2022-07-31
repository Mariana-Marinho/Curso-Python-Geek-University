# ler número inteiro positivo de 100 a 999 e inverter, ex.: 123 -> 321
num = input('digite um número entre 100 e 999: ')
num_inverso = int(num[::-1])
print(f'o inverso do número {num} é {num_inverso}')
