import datetime
import random
#Class save data on cache
class MyCache:
    def __init__(self):
        #constructor
        self.cache={}
        self.max_cache_size=10
    
    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache)>=self.max_cache_size:
            self.remove_oldest()

        self.cache[key] = {'date_accessed' : datetime.datetime.now(), 'value' : value}
    
    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry=None
        for key in self.cache:
            if oldest_entry==None:
                oldest_entry=key
            elif self.cache[key]['date_accessed']<self.cache[oldest_entry]['date_accessed']:
                oldest_entry=key
        
        self.cache.pop(oldest_entry)

    def show_keys_Values(self):
        
        for k,v in self.cache.items():
            print("=>"+k,v)
    
    @property
    def size(self):
        return str(len(self.cache))

#Decorator function
def decor_func_adding_name(func):
    def wrapper(info, name):
        return  "Added : " + name +" - "+format(func(info))
    return wrapper

@decor_func_adding_name
def show_group(group):
    return "group : "+ format(group)

#Enter Data
cache=MyCache()
while True:
    print("1. Add information \n2. Quit")
    choose=input("Enter number you choose : ")
    if choose=='1':
        name_input = input("Enter your name : ")
        group_input = input("Enter your group : ") 
        print("Cache size : ", cache.size) 
        print("============= Data in cache : =============")
        cache.show_keys_Values()
        print (show_group(group_input, name_input))
        cache.update(name_input, group_input)
    elif choose=='2':
        break


