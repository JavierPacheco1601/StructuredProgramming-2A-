#include <stdio.h>
#include <stdlib.h> //atoi
#include <string.h> // strcpy //


int my_int = 0; // %i o %d
float my_float = 3.14; // %f
char my_char = 'c'; // %c
char my_str [10] = "Hola"; // %s

float second_float = 0.0;

// Pointer //
int* my_ptr_int = &my_int; // %p


int main( int argc, char** argv){
        // pegando el argv1 a la var string
        strcpy(my_str, argv[1] );
        // convertir string a intero
        int base = atoi(my_str);

        strcpy(my_str, argv[2] );
        int altura = atoi(my_str);

        printf( "my_int: %i, my_float; %f, my_char: %c, my_str: %s, my_ptr_int: %p. \n", my_int, my_float, my_char, my_str, my_ptr_int);
        printf( "argc: %i, element 1: %s, elem 2: %s char: %c \n", argc, argv[1], argv[2], 'L' );

        return 0;