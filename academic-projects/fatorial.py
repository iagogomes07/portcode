def fatorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


n = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = fatorial(n)
if resultado is not None:
    print(f"{n}! = {resultado}")
else:
    print("Não é possível calcular fatorial de número negativo.")