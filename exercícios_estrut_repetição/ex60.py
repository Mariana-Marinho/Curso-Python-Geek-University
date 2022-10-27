"""
Ler vários números e informar
1- soma dos números
2- a quantidade de números digitados
3- média
4- o maior digitado
5- o menor digitado
6- a média dos pares
"""
soma = quantidade = menor = maior = media_pares = pares = 0
while True:
    num = float(input('digite um número: '))
    if num == 0:
        break
    quantidade += 1
    soma += num
    if quantidade == 1 or num < menor:
        menor = num
    if quantidade == 1 or num > maior:
        maior = num
    if num % 2 == 0:
        media_pares += num
        pares += 1
print(f"""
1- soma dos números = {soma}
2- a quantidade de números digitados = {quantidade}
3- média = {soma/quantidade}
4- o maior digitado = {maior}
5- o menor digitado = {menor}
6- a média dos pares = {media_pares/pares}
""")
