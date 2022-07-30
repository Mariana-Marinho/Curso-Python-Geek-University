# programa que lê as coordenadas x e y de pontos no R2 e calcular a distância da origem
x = float(input('informe a coordenada x do ponto: '))
y = float(input('informe a coordenada y do ponto: '))
distancia = ((x**2)+(y**2))**(1/2)
print(f'a distância do ponto de coordenadas {x, y} à origem vale {distancia:.2f}')
