# -*- coding: utf-8 -*-
"""
# MAP & ZİP & REDUCE & FİLTER

## Map
"""

numbers = [39,24,11,25,64,81]

def square(number):
  return number ** 2

print(list(map(square, numbers))

numbers = [39,24,11,25,64,81]
print(list(map(lambda x : x*x , numbers)))

num1 = [14,26,11,32,84]
num2 = [12,32,66,14,17]

def min(x,y):
  if x < y:
    return x
  return y

print((list(map(min, num1, num2))))

"""## Zip"""

age = [22,24,26,28]
name = ['Julia', 'John']

print(list(zip(name, age)))

"""## Reduce"""

from functools import reduce

num = [11,3,9,12,4,15,66]

def find_max(a,b):
  if a > b:
    return a
  return b

print(reduce(find_max, num))

num = [2,4,6,8,10,12]
def cal(a,b):
  return a*b

print(reduce(cal, num))

"""## Filter"""

x = ['Hello','Data','Science','Researchers']

print(list(filter(lambda word: len(word) >=6, x)))

print(list(map(lambda word: len(word), x)))
