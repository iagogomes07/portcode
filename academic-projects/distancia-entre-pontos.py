import math
print('Insira os valores dos pontos P (x1,y1) e Q (x2,y2) abaixo:')
x1 = float(input('Digite a coordenada x1: '))
y1 = float(input('Digite a coordenada y1: '))
x2 = float(input('Digite a coordenada x2: '))
y2 = float(input('Digite a coordenada y2: '))
x = (x2 - x1)**2
y = (y2 - y1)**2
d = math.sqrt(x + y)
print(f'A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é: {d:.2f}')