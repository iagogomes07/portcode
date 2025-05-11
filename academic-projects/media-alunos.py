a = 0
b = 0
c = 0
print('Digite [-1] para sair')
while True:
    d = float(input('Digite a nota:'))
    if d == -1:
        break
    c += 1
    if d < 5.0:
        b = b + 1
    else:
        a = a + 1
print(f'{c} alunos fizeram a prova')
print(f'{a} alunos foram aprovados')
print(f'{b} alunos foram reprovados')