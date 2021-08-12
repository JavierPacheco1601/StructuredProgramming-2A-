from sys import argv
#list container
lista = [ "Red", "Black", "White" ]
##List Comp.
lista2 = [i for i in range (1, 101) if i%2==2 ]

listaEvenOdd = [ [i for i in range  (1, 101) if i%2==0 ], [i for i in range (1, 101) if i%2!=0] ]
print(listaEvenOdd)
if __name__ == "__main__" :
        print(  f'programName: {argv[0]}\n'   )
        print( lista, len( lista ) ) #Size of a list
        ## Manual
        # print(  lista[0]    )
        # print(  lista[1]    )
        # print(  lista[2]    )
        # print(  lista[3]    )
        ##...
        ##...
        ## Auto
        index = 0
        while(  index < len(lista)  ):
                print( f'index:{index}, value: {lista[index]} ')
                index = index + 1
        print("-------------------")
        for index in range (0, len(lista) ):
                print(f'index:{index},  value {lista[index]}')
                