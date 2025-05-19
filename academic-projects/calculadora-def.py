def soma(a, b):
    print(f"Resultado: {a + b}")

def subtracao(a, b):
    print(f"Resultado: {a - b}")

def multiplicacao(a, b):
    print(f"Resultado: {a * b}")

def divisao(a, b):
    if b != 0:
        print(f"Resultado: {a / b}")
    else:
        print("Erro: divisão por zero!")


a = float(input("Digite o primeiro valor: "))
operador = input("Digite a operação (+, -, x, /): ")
b = float(input("Digite o segundo valor: "))

if operador == '+':
    soma(a, b)
elif operador == '-':
    subtracao(a, b)
elif operador.lower() == 'x':
    multiplicacao(a, b)
elif operador == '/':
    divisao(a, b)
else:
    print("Operador inválido!")