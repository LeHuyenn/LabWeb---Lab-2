firstList = []
secondList = []
thirdList = []
inputList=[1,2,3,4,5,6]

#Main function hadle requirement
def func(lIn):
    for x in lIn:
       if x%2 == 0:
          firstList.append(x)
       elif x%3 == 0 :
          secondList.append(x)
       elif x%5 == 0:
          thirdList.append(x)


func(inputList)
print("First List : ", firstList)
print("Second List : ", secondList)
print("Third List : ", thirdList)
