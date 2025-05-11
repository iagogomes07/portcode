#contador ordem crescente
print('numeros naturais na horizontal')
a = int(input('insira o numero inicial: '))
b = int(input('insira o numero final: '))
c = int(input('insira o intervalo: '))
d = 0
for a in range(a, b + 1, c):
    if a < b -1:
        print(a, end=",")
    else:
        print(a, end = ".")

    d = d + 1
print('\nrepetição encerrada')
print(f'valores gerados: {d}')
