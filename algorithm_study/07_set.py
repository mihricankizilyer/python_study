# -*- coding: utf-8 -*-
"""
set
"""

x = [1,1,2,2,3,3,4,4,5]

x = [1,2,3,1,2,3,4,4,5]
y = [1,2,3,4,5]
y = set(x)

for i in y:
    count = 0
    for k in x:
        if k ==i:
            count +=1
    print("{}.sayı {} var".format(i,count))
    if count == 1:
        print(i)
        
#with func
def find_single_value(x):
    y = set(x)
    for i in y:
        count = 0
        for k in x:
            if k == i:
                count +=1
        if count == 1:
            return i
            
find_single_value([1,1,2,2,3,3,4,4,5,5,6])
