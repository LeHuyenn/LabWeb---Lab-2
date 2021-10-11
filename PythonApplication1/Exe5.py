#Main function
def func(valForCheckPrime):
    if valForCheckPrime<2:
        return False
    else:
        for i in range(2, valForCheckPrime):
            if valForCheckPrime%i==0:
                return False
    return True

#Enter Number
i=0
valInput=0
while i<10:
    while True:
        try: 
            valInput=int(input("Enter your number(from 0 to 100000): "))
            if valInput<0 or valInput >100000:
                print("Your input value have to be a number in range [0 ; 100000]! Please enter again!")
                i=0
            else:
                i=20
                break
        except ValueError:
            print ("Your input value is not int! Please enter again!")
            i=0

print("Number is prime! : ", func(valInput))
