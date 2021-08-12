#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include "./foldertest/utils.h"
#include "stdbool.h"
void callToNumber(int number){
        //Logica compleja para llamar a un numero//
        printf("Llamando al %d...!\n", number   );
}
//Declarando
void SecurityCamera( void (*callToNumber) (int number),  int  EmergencyNumber );
int main(){
        
        // for(;;){
                SecurityCamera( callToNumber, 911  );

        // }
        return 0;
}
//Defi
void SecurityCamera( void (*callToNumber) (int number), int EmergencyNumber   ){
        //Logica Compleja//
        bool thief = false;
        if(thief){ //Si detecta ladron debe hacer algo!
                // Ejecutar un calback
                callToNumber(EmergencyNumber);
        }
}