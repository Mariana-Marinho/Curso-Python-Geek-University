# imprimir o ano de uma pessoa a partir de sua idade atual
from datetime import date
ano = date.today().year
idade = int(input(f'digite sua idade atual no ano de {ano}: '))
ano_nasc = ano-idade
print(f'você nasceu no ano {ano_nasc}, correto?')
