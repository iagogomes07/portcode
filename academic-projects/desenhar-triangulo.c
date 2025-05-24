#include<stdio.h>

int main(){
    int  a, b, i;
    printf("Insira um numero inteiro:");
    scanf("%d", &a);

    for(i = 1; i <= a; i++){
        for(b = 1; b <= i; b++){
                printf("*");

        }printf("\n");
    } 
return 0;
}