#include <stdio.h>
#include <cs50.h>
int main(void)
{
    string x = get_string("tell me your name ");
    printf("hello, %s\n", x);
}
