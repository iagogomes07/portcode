#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// Função para converter de qualquer base para decimal
long base_para_decimal(char *numero, int base_origem) {
    long decimal = 0;
    int tamanho = strlen(numero);
    int potencia = 0;
    
    // Processa cada dígito da direita para esquerda
    for (int i = tamanho - 1; i >= 0; i--) {
        char c = toupper(numero[i]);
        int valor;
        
        // Converte caracteres para valores (0-15)
        if (c >= '0' && c <= '9') {
            valor = c - '0';
        } else if (c >= 'A' && c <= 'F') {
            valor = 10 + (c - 'A');
        } else {
            printf("Dígito inválido: %c\n", c);
            return -1;
        }
        
        // Verifica se o dígito é válido para a base
        if (valor >= base_origem) {
            printf("Dígito %c inválido para base %d\n", c, base_origem);
            return -1;
        }
        
        decimal += valor * pow(base_origem, potencia);
        potencia++;
    }
    return decimal;
}

// Função para converter de decimal para qualquer base
void decimal_para_base(long decimal, int base_destino, char *resultado) {
    char digitos[] = "0123456789ABCDEF";
    int indice = 0;
    
    if (decimal == 0) {
        resultado[0] = '0';
        resultado[1] = '\0';
        return;
    }
    
    // Converte o número
    while (decimal > 0) {
        int resto = decimal % base_destino;
        resultado[indice++] = digitos[resto];
        decimal = decimal / base_destino;
    }
    resultado[indice] = '\0';
    
    // Inverte a string para obter o resultado correto
    for (int i = 0; i < indice / 2; i++) {
        char temp = resultado[i];
        resultado[i] = resultado[indice - 1 - i];
        resultado[indice - 1 - i] = temp;
    }
}

int main() {
    char numero[50];
    char resultado[50];
    int base_origem, base_destino;
    
    printf("\n--- CALCULADORA DE BASES NUMÉRICAS (2 a 16) ---\n");
    
    // Entrada do usuário
    printf("Digite o número a ser convertido: ");
    scanf("%s", numero);
    
    printf("Base de origem do número (2-16): ");
    scanf("%d", &base_origem);
    
    printf("Base de destino (2-16): ");
    scanf("%d", &base_destino);
    
    // Validação das bases
    if (base_origem < 2 || base_origem > 16 || base_destino < 2 || base_destino > 16) {
        printf("Erro: Bases devem estar entre 2 e 16.\n");
        return 1;
    }
    
    // Conversão para decimal
    long valor_decimal = base_para_decimal(numero, base_origem);
    if (valor_decimal == -1) {
        return 1;
    }
    
    // Conversão para base destino
    if (base_destino == 10) {
        printf("\nResultado: %s (base %d) = %ld (base 10)\n", numero, base_origem, valor_decimal);
    } else {
        decimal_para_base(valor_decimal, base_destino, resultado);
        printf("\nResultado: %s (base %d) = %s (base %d)\n", numero, base_origem, resultado, base_destino);
    }
    
    return 0;
}