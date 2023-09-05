#include <stdio.h>

int main(void)
{
    char nome[30];
    printf("Qual o seu nome? ");
    scanf("%s", nome);
    printf("Ola, %s!\n", nome);

    return 0;
}