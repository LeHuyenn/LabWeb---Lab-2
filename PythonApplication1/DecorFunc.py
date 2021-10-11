
#Cach 1
def func1(output):
    output=output+1
    return "output:"+ format(output)

def decor_func(func):
    def wrapper(info):
        return "Add at the first "+format(func(info))
    return wrapper

x = decor_func(func1)
print(x(2))

#Cach 2: dua @<Ten ham decor> len tren ham can decor
def decor_func2(func):
    def wrapper(info,add):
        return "Add at the first "+format(func(info))+add
    return wrapper
@decor_func2
def func2(output):
    output=output+1
    return "output:"+ format(output)

print(func2(2,'LOLO'))