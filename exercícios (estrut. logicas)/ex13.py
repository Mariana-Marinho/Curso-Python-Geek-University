# média ponderada de uma nota
from numpy import arange
trabalho = float(input('digite a nota do trabalho de laboratório: '))
avaliacao = float(input('digite a nota da sua avaliação semestral: '))
final = float(input('digite a nota da sua avaliação final: '))
# usando o arange para criar um intervalo com float (usando step de 0.01)
if trabalho in arange(0, 10, 0.01) and avaliacao in arange(0, 10, 0.01) and final in arange(0, 10, 0.01):
    media = (trabalho*2+avaliacao*3+final*5)/10
    if media < 3:
        print(f'como sua média foi {media}, você ficou de recuperação...')
    elif 3 <= media < 5:
        print(f'sua media foi {media}, então você ficou de recuperação')
    else:
        print(f'PARABÉNS VOCÊ PASSOU!!!! Sua média ficou {media}')
else:
    print('digite notas válidas')
