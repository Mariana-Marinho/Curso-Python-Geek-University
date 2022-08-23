"""
Classificar um nadador numa categoria de acordo com a idade
"""

nome = str(input('Digite o nome do atleta: '))
i = int(input('Digite a idade do atleta: '))
if i < 5:
    print(f'atleta muito jovem, tente daqui a {5-i} anos')
else:
    if i in range(5, 8):
        print('o atleta está na categoria Infantil A')
    elif i in range(8, 11):
        print('categoria Infantil B')
    elif i in range(11, 14):
        print('categoria Juvenil A')
    elif i in range(14, 17):
        print('categoria Juvenil B')
    else:
        print('categoria Sênior')
