print('numeros naturais na horizontal')
a = int(input('insira o numero inicial: '))
b = int(input('insira o numero final: '))
c = int(input('insira o intervalo: '))
if a > b:
    for x in range(a, b - 1, -c):
        if x > b:
            print(x, end=',')
        else:
            print(x, end ='.')
else:
    for x in range(a, b + 1, c):
        if x < b:
            print(x, end=",")
        else:
            print(x, end=".")

