#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }

while (h>8 || h<1);

for (int i = 0; i < h; i++)

{

    for (int j=h-i; j>1; j--)

    {
        printf(" ");
    }

    for (int j = 0; j <= i; j++)

    {
        printf("#");
    }
    printf("  ");

    for (int j = 0; j<= i; j++)

    {
        printf("#");
    }

    printf("\n");

}

}
