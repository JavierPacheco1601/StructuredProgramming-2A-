#include <stdio.h>
#include <stdlib.h>  // atoi, atof 
#include <stdbool.h>


#define TAN 10

int lista[TAN] =  { 105,20,21,40,33,60,70,50,93,100 };
int idx =  0 ;



typedef int INTEGER;


int main(int argc, char** argv ){

        int index2 = 0;
        for( int index = 1; index <= TAN; index++, index2++  ){

                printf( "index: %d, value: %d.\n\a", index,  lista[index]  );
                for (INTEGER i = 0; i <3; i++)
                {
                        /* code */
                }

                
                
                
        }


        while (  true    )
        {       
                if(   lista[idx] == 50   ){
                        break;
                }
                idx++;
        }
        printf( " idx found:  %d\n", idx    );

        
        int idx_for =0;
        for( ;   lista[idx_for] != 50; idx_for++     ){ }
        printf( " idx_for found:  %d", idx_for    );
        return 0;
}