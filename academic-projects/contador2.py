#contador ordem decrescente
print('numeros naturais na horizontal')
a = int(input('insira o numero inical: '))
b = int(input('insira o numero final: '))
c = int(input('insira o intervalo: '))
d = 0
for a in range(a, b + 1, -c):
    print(a, end = ',')
    d = d + 1
print('\nrepetição encerrada')
print(f'valores gerados: {d}')