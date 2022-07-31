# ler quanto cada um dos 3 apostadores investiu e dividir o prêmio proporcionalmente
ap1 = float(input('digite o quanto o 1o apostador investiu: '))
ap2 = float(input('digite o quanto o 2o apostador investiu: '))
ap3 = float(input('digite o quando o 3o apostador investiu: '))
premio = float(input('digite o valor do prêmio: '))
v1 = premio*ap1/(ap3+ap2+ap1)
v2 = premio*ap2/(ap3+ap2+ap1)
v3 = premio*ap3/(ap3+ap2+ap1)
print(f"""
o prêmio de {premio:.2f} será dividido da seguinte forma:
1-> o primeiro apostador ganhará {v1}
2-> o segundo apostador ganhará {v2}
3-> o terceiro apostador ganhará {v3}
""")
