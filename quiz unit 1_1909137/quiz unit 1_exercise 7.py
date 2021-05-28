start program
num1= 0
num2=0
num3=0
gnum=0 

num1=int(input("Write the first number: "))
num2=int(input("Write the second number: "))
num3=int(input("Write the third number: "))

if(num1 > num2):
    if (num1> num3):
        gnum=num1
    else:
        if(num3> num2):
            gnum=num3
else:
    if (num2> num3):
        gnum= num2
    else:
        gnum=num3

print("The gratest number among the three is: ", gnum)
end program