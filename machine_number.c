#include <stdio.h>
#include <limits.h>
#include <float.h>

// Print maximum and minimum machine mumbers for different data types using C

int main() {
    printf("Maximum and Minimum values for char: %d to %d\n", CHAR_MIN, CHAR_MAX);
    printf("Maximum and Minimum values for int: %d to %d\n", INT_MIN, INT_MAX);
    printf("Maximum and Minimum values for long int: %ld to %ld\n", LONG_MIN, LONG_MAX);
    printf("Maximum and Minimum values for float: %e to %e\n", FLT_MIN, FLT_MAX);
    printf("Maximum and Minimum values for double: %le to %le\n", DBL_MIN, DBL_MAX);

    return 0;
}
