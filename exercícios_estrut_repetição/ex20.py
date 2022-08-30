"""
Ler números e dizer se são pares ou não
"""
dados = pares = 0
num = 0
while True:
    num = int(input('digite um valor (1000) para parar: '))
    if num == 1000:
        break
    else:
        dados += 1
        if num % 2 == 0:
            pares += 1
print(f'foram digitados {dados} números, dos quais {pares} foram pares')
