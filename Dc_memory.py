#include <stdio.h>
#include <stdlib.h>


int array[5];
int* arrayPointer = NULL;

int*  arreglo  = NULL;

int main(){



        arrayPointer =  (int*)malloc( 6 * sizeof(int)  );
        arrayPointer[0] =  35;
        arrayPointer[1] =  36;
        arrayPointer[2] =  37;
        arrayPointer[3] =  38;
        arrayPointer[4] =  31;
        arrayPointer[5] =  30;
        for(int index = 0;  index<6;  index++  ){
                printf( "arrayPointer[%d]: '%d'\n  "  , index,   arrayPointer[index] );
        };
        printf( "------------\n  ");
        arreglo = (int*)calloc( 6, sizeof(int)  );
        for(int index = 0;  index<6;  index++  ){
                printf( "arreglo[%d]: '%d'\n  "  , index,   arreglo[index] );
        };

        arrayPointer =   realloc(arrayPointer, 10*sizeof(int)    );
        arrayPointer[6] =  29;
        arrayPointer[7] =  28;
        arrayPointer[8] =  25;
        arrayPointer[9] =  24;
        printf( "------------\n  ");
        for(int index = 5;  index<10;  index++  ){
                printf( "arrayPointer[%d]: '%d'\n  "  , index,   arrayPointer[index] );
        };
        free(arrayPointer);

        return 0;