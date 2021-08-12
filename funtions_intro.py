from sys import argv as ag


def addToNumbers( number1,  number2   ):
        print('StartProgram: addToNumbers executed...\n')
        result = number1+number2

        return result

answer =  False

def isEven( aNumber  ):
        if( aNumber%2 == 0 ):
                return True
                # print("it's even" )
        else:
                return False
                # print("it is odd!")

## isPrime

        
if __name__  == "__main__":
        # print(f' La suma de dos numeros =  {  addToNumbers(  int(ag[1]  ), int(ag[2])   )   } ')
        n1 = int(  input(   'Dame numero 1:\t'   )   )
        n2 = int( input('Dame numero 2:\t'))


        # print(  f'  La suma de dos numeros =  {  addToNumbers( n1, n2     )  } '  )
        # answer = isEven(    addToNumbers( n1, n2) )
        if(   isEven(    addToNumbers( n1, n2) )   ):
                print( f'N1: "{n1}"  and N2: "{n2}"  are your lucky numbers!'   )
        else:
                print(  f'N1: "{n1}" and N2: "{n2}" are NOT your lucky numbers!'   )

        # if( isPrime(  n3   ) ):
        #         print("n3 is prime")
        # else:
        #         print("n3 is not prime")

        # if( isPrime(  n4   ) ):
        #         print("n4 is prime")
        # else:
        #         print("n4 is not prime")