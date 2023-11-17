#include <stdio.h>

//  Print the size of the char, int, long int, float, double data types

int main() {
    printf("Size of char: %lu bytes\n", sizeof('N'));
    printf("Size of int: %lu bytes\n", sizeof(76));
    printf("Size of long int: %lu bytes\n", sizeof(1536789));
    printf("Size of float: %lu bytes\n", sizeof(28.6));
    printf("Size of double: %lu bytes\n", sizeof(1.23659874215367854557821));

    return 0;
}
