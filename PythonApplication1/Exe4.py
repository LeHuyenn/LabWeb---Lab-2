import math
#Handle input data, make sure data input is number
def enter_data(nameData):
    i=0
    while i<10:
        while True:
            try: 
                Input=float(input("Enter "+nameData+" = "))
                i=20
                break
            except ValueError:
                print ("Your input value is not number! Please enter again!")
                i=0
    return Input

#Main function
#Method Newton
def findx_with_method_Newton(nIn, AIn,EpsIn):
    x=1
    while True:
        xk=(1/nIn)*((nIn-1)*x+(AIn/math.pow(x,nIn-1)))
        if abs(x-xk)<EpsIn:
            break
        x=xk
    return x

#Enter data
allowEnterA=False
n=0
A=0
eps=math.pow(10,-10)
#Enter n
while True:
    n=enter_data("n (n>=0)")
    if n<0:
        print("n have to be greater than 0. Please enter n again!")
    elif n==0:
        print("while n=0, A always is 1, can not find x!")
        quit()
    else:
        allowEnterA = True
        break

#Enter A
if(allowEnterA):
    while True:
        if n%2==0:
            A = enter_data("A (A=0 or A>1)")
            if A==0 or A>1:
                break
            else:
                print("While n = ",n," A have to be greater than or equal by 0. Please enter A again!")

        else:
            A = enter_data("A (A>1)")
            if A>1:
                break
            else:
                print("While n = ",n," A have to be greater than 1. Please enter A again!")

#Output
print("x = ",round(findx_with_method_Newton(n, A,eps),3))
