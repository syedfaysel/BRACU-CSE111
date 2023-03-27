# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 00:18:18 2022

@author: rajo0
"""

list = [1, 2, 5, 2, 1, 3]

set = {1,2 ,2, 4,3}

tup = (1,2,2, 4,3)

dic = {"c":"Rajo", "a": "Faysel", "b": "Syed"}

# print(list)
# print(set)
# print(dic)
# print(tup)

# print(sorted(list))
# print(sorted(dic))
# print(sorted(set))
# print(sorted(tup))



# list.sort()

# print(type(dic.values()))
# print(type(dic.keys()))
# print(type(dic.items()))


# print(dic.keys())

# for value in dic.values():
#     print(value)
    
    

def capitalize(s):

    newS = ""
    for i in range(len(s)):
        if i == 0:
            newS += s[i].upper()

        elif (s[i] == 'i') and ((s[i+1] == " " and s[i-1] == " ") or (s[i+1] == "'")):

            newS += s[i].upper()
        
        elif (s[i-2] == '.' or s[i-2] == "?" or s[i-2] == "!"):
            newS += s[i].upper()

        else:
            newS += s[i]
        
        
    print(newS)
    
capitalize("syould i've ? may i love my pet very")
capitalize("oyay then i'll to do the task later")
capitalize("my.")