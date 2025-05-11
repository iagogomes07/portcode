a = float(input('Digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
print('Escolha a operação:')
print ('(1) para adição')
print ('(2) para subtração')
print ('(3) para multiplicação')
print ('(4) para divisão')
o = input('Digite o número da operação desejada (1, 2, 3 ou 4):')
if o == '1':
    r = a + b
    print(f'O resultado da soma é: {r}')
elif o == '2':
    r = a - b
    print(f'O resultado da subtração é: {r}')
elif o == '3':
    r = a * b
    print(f'O resultado da multiplicação é: {r}')
elif o == '4':
    if b == 0:
        r = a / b
        print(f'O resultado da divisão é: {r}')
    else:
        print('Erro: Não é possível dividir por zero')
else:
    print('Operação inválida')
