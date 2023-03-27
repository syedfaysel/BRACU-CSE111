# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:27:45 2022

@author: rajo0
"""

# All about tuple 

tup = (1, 2, 3, 5)
print(type(tup))


#  Tuples are ordered but immutable or unchangeable 
# single element also ends with comma
print(type((2,)))


print(tup.__contains__(1))


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

tup2 = (thistuple[2:])
print(tup2)

print(thistuple.__add__(tup2))


# tuple allows duplicates
# ordered, means tuple items can be accessed using index number

list = list(tup)
print(list) 

stup = set(tup)
print(stup)   
    
    
    
    
    
    
    
    
    