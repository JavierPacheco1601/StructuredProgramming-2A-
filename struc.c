#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include "./folderTest/utils.h"

int a = 2;
int b = 4;

int main(int argc, char** argv){
        int otroInt  = 9;
        UTILS myStructC = {1, ShowIntAdress }; //adding the function to link to 
        printf("myInt: %d. &myStructC: %p\n", myStructC.myInt, &myStructC );
        UTILS* myStructP = &myStructC;
        printf("myInt: %d\n", (*myStructP).myInt );
        printf("myInt: %d\n", myStructP->myInt );
        myStructC.ShowIntAdress(&otroInt );
        UTILS obj;
        obj.myInt =  100;
        obj.mySwap = swap;
        obj.mySwap(  &a, &b  );
        printf( "a:%d, b:%d.", a,b );   
        return 0;
}