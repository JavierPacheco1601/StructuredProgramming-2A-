  
from sys import argv as ag 

def palindrome(string): 
    validate = "".join(string.lower().split (" "))
    if validate [::-1] == validate:
        return True
    else:
        return False 

    print(validate)
if __name__ == "__main__":
    print( palindrome(  "amor a roma"  ))
    