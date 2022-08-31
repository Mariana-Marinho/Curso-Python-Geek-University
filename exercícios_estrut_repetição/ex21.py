"""
Receber dois números e calcular a soma dos pares e a multiplicação do números ímpares entre o intervalo dos números
"""
while True:
    try:
        numero1 = int(input('digite um número: '))
        numero2 = int(input('digite outro número: '))
        break
    except Exception as erro:
        print(f'ERROR digite números válidos: {erro}')
menor = min(numero2, numero1)
maior = max(numero2, numero1)
soma =  0
produto = 1
for num in range(menor, maior+1):
    if num % 2 == 0:
        soma += num
    else:
        produto *= num
print(f'o produto entre os números ímpares deu {produto}')
print(f'a soma entre os números pares deu {soma}')
