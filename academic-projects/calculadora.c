#include <stdio.h>

int main() {
    float a, b, x;
    int c;

    printf("Digite um numero inteiro: ");
    scanf("%f", &a);

    printf("Digite outro numero inteiro:");
    scanf("%f", &b);

    printf("Digite [1] para +, [2] para -, [3] para *, [4] para /");
    scanf("%d", &c);

switch (c){
    case 1:
        x = a + b;
        printf("O valor somado e igual a: %f", x);
        break;
    case 2:
        x = a - b;
        printf("O valor subtraido e igual a: %f", x);
        break;
    case 3:
        x = a * b;
        printf("O valor multiplicado e igual a: %f", x);
        break;
    case 4:
        x = a / b;
        printf("O valor dividido e igual a: %f", x);
        break;
    default:
        printf("Digita uma operacao valida ai man");

    }

    return 0;
}