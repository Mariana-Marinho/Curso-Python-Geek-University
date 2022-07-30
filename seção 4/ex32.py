# ler um número e imprimir a soma do sucessor de seu triplo com o antecessor do dobro
numero = int(input('digite um número: '))
sucessor_triplo = numero*3+1
antecessor_dobro = numero*2-1
print(f'a soma do sucessor do triplo de {numero}, {sucessor_triplo}, com o antecessor do seu dobro, {antecessor_dobro},'
      f' é {sucessor_triplo+antecessor_dobro}')
