# ler o horário de início e duração de uma experiência, retornando o término do experimento
from datetime import timedelta
ini_hora = int(input('digite a hora do início do experimento: '))
ini_min = int(input('digite os minutos do início: '))
ini_seg = int(input('agora os segundos: '))
duracao = int(input('digite a duração do experimento em segundos: '))
fim = (ini_hora*60*60)+(ini_min*60)+ini_seg+duracao
fim = timedelta(seconds=fim)
print(f'o horário de término do experimento foi às {fim}')
