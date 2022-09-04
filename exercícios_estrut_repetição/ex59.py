"""
Ler os habitantes de uma cidade, o valor do kwh, consumo e código de cada um
"""
hab = int(input('número de habitantes da cidade: '))
kwh = float(input('valor do kwh: '))
res = []
com = []
ind = []
for i in range(0, hab):
    codigo = int(float('1 - Residencial\n2 - Comercial\n3 - Industrial\n'))
    consumo = float(input('consumo: '))
    if codigo == 1:
        res.append(consumo)
    elif codigo == 2:
        com.append(consumo)
    else:
        ind.append(consumo)
print(f"""
o maior consumo residencial foi {max(res)} e o menor foi {min(res)}
1 - média do residencial {sum(res)/len(res)}
2 - média do comercial {sum(com)/len(com)}
3 - média do industrial {sum(ind)/len(ind)}""")
