import sys

###Practica###

def order (a):
    return[sorted([a[i] for i in range (0, len(a)) if a[i]>0 ])]

if __name__ == "__main__":
    a=[-1,150,190,170,-1,-1,160,180]
    
    print(order(a))