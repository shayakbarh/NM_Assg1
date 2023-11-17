// main.c
#include <stdio.h>
#include <stdlib.h>
#include "stats.h"

int main() {
   float*my_array;
    my_array=(float*)calloc(100, sizeof(float));

    for (int i = 1; i < 101; i++)
    {
        float squaredValue = (float)i * i;
        printf("Element %d: %f\n", i, squaredValue);
        my_array[i-1]=i*i;
    }

    float result[2]; // initializing the length of the array
    mean_variance(my_array, 100, result);

    // Print mean and variance
    printf("Mean: %f\n", result[0]);
    printf("Variance: %f\n", result[1]);

    // Write the result to a text file
    FILE *textFile = fopen("result.txt", "w");
    fprintf(textFile, "Mean: %f\n", result[0]);
    fprintf(textFile, "Variance: %f\n", result[1]);
    fclose(textFile);

    

     // Free the allocated memory
    free(my_array);
    return 0;
}