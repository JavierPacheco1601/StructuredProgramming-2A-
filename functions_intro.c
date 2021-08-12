#include <stdio.h>
// #include "./utils.h"
#include "./foldertest/utils.h"

int myNumber = 3;
float myFloat  = 3.1416;
char myString[255] = "Hola mundo";

int main(  ){
        sayHello(  "Hello world" ); 
        sayMyName( "Luis" );
        int myResult =     addTwoNumbers(  2, 5   );
        printf( "myResult is equal to:  %d \n",   myResult  );
        printf("%d", libInteger  );
        return 0;
}