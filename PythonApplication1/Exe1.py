#Main function handle requirement
i=0
def func(inValue, len):
    slicedString=str(inValue)[len::-1]
    if int(slicedString)==inValue:
        print("TRUE!")
    else:
       print("FALSE!")

#Enter Number
while i<10:
    while True:
        try: 
            valInput=int(input("Enter your number(>9): "))
            if len(str(valInput))<=1 or valInput <1:
                print("Your input value have to be a number greater than 9! Please enter again!")
                i=0
            else:
                i=20
                break
        except ValueError:
            print ("Your input value is not int! Please enter again!")
            i=0



func(valInput,len(str(valInput)))






