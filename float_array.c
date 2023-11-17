/*
    Using the malloc standard library function to create an array of hundred float elements 
    and assigning the values 1^2,2^2,......,100^2 to the elements of this array.

*/ 

#include<stdio.h>
#include<stdlib.h>

int main()
{  
    // Using malloc to allocate memory for an array of 100 floats
    float*array;
    array=(float*)malloc(100*sizeof(float));

    for( int i=0; i<100; i++)
    {
        array[i]=(i+1)*(i+1);
    }

    
    // Printing the array elements
    printf("Array elements: ");
    for(int i=0; i<100; i++)
    {
        printf("%.2f ", array[i]);
        
    }

    printf("\n");



    return 0; // Return 0 to indicate successful execution

}