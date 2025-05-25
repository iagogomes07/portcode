def base_para_decimal(numero, base_origem):
    """Converte um número de qualquer base (2-16) para decimal."""
    digitos = '0123456789ABCDEF'
    numero = str(numero).upper()
    decimal = 0
    for i, digito in enumerate(reversed(numero)):
        valor = digitos.index(digito)
        decimal += valor * (base_origem ** i)
    return decimal

def decimal_para_base(decimal, base_destino):
    """Converte um número decimal para qualquer base (2-16)."""
    digitos = '0123456789ABCDEF'
    if decimal == 0:
        return '0'
    resultado = []
    while decimal > 0:
        resto = decimal % base_destino
        resultado.append(digitos[resto])
        decimal = decimal // base_destino
    return ''.join(reversed(resultado))

def calculadora_base():
    print("\n--- CALCULADORA DE BASES NUMÉRICAS (2 a 16) ---")
    
    # Entrada do usuário
    numero = input("Digite o número a ser convertido: ").strip().upper()
    base_origem = int(input(f"Base de origem do número (2-16): "))
    base_destino = int(input(f"Base de destino (2-16): "))
    
    # Validação das bases
    if not (2 <= base_origem <= 16) or not (2 <= base_destino <= 16):
        print("Erro: Bases devem estar entre 2 e 16.")
        return
    
    # Conversão
    try:
        # Para decimal primeiro
        if base_origem != 10:
            valor_decimal = base_para_decimal(numero, base_origem)
        else:
            valor_decimal = int(numero)
        
        # De decimal para base destino
        if base_destino != 10:
            resultado = decimal_para_base(valor_decimal, base_destino)
        else:
            resultado = str(valor_decimal)
        
        print(f"\nResultado: {numero} (base {base_origem}) = {resultado} (base {base_destino})")
    
    except ValueError:
        print("Erro: Número inválido para a base informada.")

# Executa a calculadora
if __name__ == "__main__":
    calculadora_base()