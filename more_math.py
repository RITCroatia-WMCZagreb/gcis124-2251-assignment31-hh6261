'''
@ASSESSME.USERID: hh6261
@ASSESSME.AUTHOR: Hana Hebib
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''

import math

def fact(b):
    if b > 0 and isinstance(n, int):
        return math.factorial(b)
    else:
        return 0
    

def root (b1):
    if b1 > 0:
        return math.sqrt(float(b1))
    else:
        return 0
    
def trunk(b2):
    return math.trunc(b2)



def main():
   b = int(input("Enter a numeric value: "))
   print(b,"factorial=", fact(b))

   b1 = float(input("Enter a numeric value: "))
   print("The square root of",b1,"=",root(b1))

   b2 = float(input("Enter a numeric value: "))
   print(b2,"truncated:", trunk(b2))



if __name__ == "__main__":
    main()