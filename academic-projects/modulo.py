def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return numero * -1


numero = float(input("Digite um número: "))
absoluto = valor_absoluto(numero)
print(f"O valor absoluto é: {absoluto}")