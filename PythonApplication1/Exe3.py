#Main function handle requirement
def func(valInputFunc):
    slicedString=str(valInput)[len(str(valInput))::-1]
    output=""
    if valInput < 0:
        slicedString = slicedString[:-1]
        output = int("-"+slicedString[:1]+slicedString[1:])
    else:
        output = int(slicedString)
    print("output: ",output)

#Enter number
i=0
valInput=0
while i<10:
    while True:
        try: 
            valInput=int(input("Enter your number: "))            
            i=10
            break
        except ValueError:
            print ("Your input value is not int! Please enter again!")
            i=0

func(valInput)