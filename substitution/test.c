#ifdef __STDC_ALLOC_LIB__
#define __STDC_WANT_LIB_EXT2__ 1
#else
#define _POSIX_C_SOURCE 200809L
#endif
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include <stdlib.h>

int main (void)
{

char y = get_char("what char?: ");
char*alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char*x;
x = strchr(alphabet, 'y');
printf("%s\n", x);
}