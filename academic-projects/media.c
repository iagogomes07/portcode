#include <stdio.h>

#define TAM 30

int main(){
	float n[TAM], soma = 0, ma, me;
	int apr = 0, rep = 0, a, b, c;

	for(a = 0; a < TAM; a++ ){

    	printf("insira a nota do aluno %d:\t", a + 1);
    	scanf("%f", &n[a]);

    	while(n[a] < 0 && n [a] > 10 ){

        	printf("insira uma nota entre 0 e 10:\t");
        	scanf("%f", &n[a]);
    	}
	}

	ma = me = n[0];

	for(a = 0; a < TAM; a++){

    	soma = soma + n[a];

    	if(n[a] > ma)
        	ma = n[a];

    	if(n[a] < me)
        	me = n[a];

    	if(n[a] > 5.9)
        	apr++;
    	else
            rep++;

	}
printf("\n \n \t |||RESUMO DA TURMA||| \t \n \n");
printf("media da turma: %.2f\n", soma / TAM);
printf("maior nota: %.2f\n", ma);
printf("menor nota: %.2f\n", me);
printf("alunos aprovados: %d\n", apr);
printf("alunos reprovados: %d\n", rep);

printf("\ndeseja consultar a nota de um aluno? [1] para sim e [2] para nao:\t");
scanf("%d", &b);

if(b == 1){
	while(1){

    	printf("\ninsira o numero do aluno ou [-1] para sair:\t", n);
    	scanf("%d", &c);

    	if(c == -1){
        	printf("\n \t|||consulta encerrada|||");
        	break;
    	}
    	if(c >= 1 && c <= TAM && c != 0){
        	printf("nota do aluno %d: %.2f\n", c, n[c - 1]);
    	}else{
    	printf("\n \t|||numero invalido|||");
    	}
	}

}else{
printf("\n \t|||consulta de notas ignorada|||");
}
}

