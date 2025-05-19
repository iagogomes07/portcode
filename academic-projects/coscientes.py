def positivo_nulo_negativo(numero):
    if numero > 0:
        print("Valor Positivo")
    elif numero == 0:
        print("Valor nulo")
    else:
        print("Valor negativo")

# Programa principal
numero = float(input("Digite um número: "))
positivo_nulo_negativo(numero)