"""
Ler um input e colocá_lo no formato de horas
"""
entrada = input('de que horas você entrou? HH:MM\n').split()
for tempo in entrada:
    hora, minuto = [int(i) for i in tempo.split(":")]
    print(f'{hora} horas e {minuto} minutos')
