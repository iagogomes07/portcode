a = 0
b = 0
mp = 0
mi = 0
print('Digite [0] para sair')
while True:
    d = float(input('Digite um número:'))
    if d == 0:
        break
    if d % 2 == 0:
        a = a + d
        mp = mp + 1
        m1 = a / mp
    else:
        b = b + d
        mi = mi + 1
        m2 = b / mi
print(f'A média dos números pares é {m1}')
print(f'A média dos números impares é {m2}')