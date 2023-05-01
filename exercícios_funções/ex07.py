"""
Converter temperatura
"""


def celsius_to_farenheit(celsius):
    f = celsius*(9/5) + 32
    return f


c = float(input('digite a temperatura em celsius: '))
print(f'{c}ºC vale {celsius_to_farenheit(c)}ºF')
