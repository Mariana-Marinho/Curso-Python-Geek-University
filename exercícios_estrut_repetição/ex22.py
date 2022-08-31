"""
Ler sequência de notas e mostrar média aritmética
"""
boletim = []
while True:
    try:
        nota = float(input('digite uma nota entre 10 e 20: '))
        if 10 <= nota <= 20:
            boletim.append(nota)
        else:
            break
    except Exception as erro:
        print(f'ERROR digite uma nota válida: {erro}')
media = sum(boletim)/len(boletim)
print(f'a média aritmética das notas foi: {media}')
