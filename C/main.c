#include <cs50.h>
#include <stdio.h>

/**
 * Função main:
 */
int main(void)
{
    // Obtém menor número do usuário (no mínimo 1):
    int min;
    do
    {
        min = get_int("Menor número: ");
    }
    while (min < 1);

    // Obtém maior número do usuário (tem que ser maior do que o min):
    int max;
    do
    {
        max = get_int("Maior número: ");
    }
    while (min >= max);

    // TODO: escreva aqui o código para imprimir todos os números primos dentro
    // da faixa especificada pelo usuário. Pode ser útil utilizar dois loops (um
    // dentro do outro) e algumas estruturas condicionais. O operador módulo
    // também pode ser útil!
    for (int v = min; v <= max; v++)
    {
        int is_prime = 1;
        if (v <= 1)
            is_prime = 0;
        else
        {
            for (int i = 2; i * i <= v; i++)
            {
                if (v % i == 0)
                {
                    is_prime = 0;
                    break;
                }
            }file:

        }

        // Verifica se é primo e imprime:
        if (is_prime)
        {
            printf("%i\n", v);
        }
    }

    // Finaliza o programa:
    return 0;
}