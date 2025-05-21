def supersayajin (a, b):
    print(f'{a} + {b} = {a + b}')
def subaton (a, b):
    print(f'{a} - {b} = {a - b}')
def menoth (a, b):
    print(f'{a} x {b} = {a * b}')
def danone (a, b):
    if b != 0:
        print(f'{a} / {b} = {a / b}')
    else:
        print(f'como q joão vai dividir {a} bananas por {b} zé')

a = float(input('digite o primeiro valor:'))
b = float(input('digite o segundo valor:'))
operra = str(input('\n(+)\n(-)\n(x)\n(/)\nescolha a operação:'))

if operra == '+':
    supersayajin(a, b)
elif operra == '-':
    subaton(a, b)
elif operra == 'x':
    menoth(a, b)
elif operra == '/':
    danone(a, b)
else:
    print('escolhe um operador certo')