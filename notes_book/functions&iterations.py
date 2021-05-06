# -*- coding: utf-8 -*-
"""
# Chapter 1 & 2 & 3 & 4 & 5

## Math functions
"""

import math

x = 20
y = 10 * math.log10(x)
z = math.sin(23)
d = math.sqrt(x)
print("Log20: ",y)
print("sin23: ",z)
print("sqrt(20):",d)

"""## Random numbers"""

import random

for i in range(5):
  x = random.random()
  print(x)
#This program produces the following list of 5 random numbers between 0.0 and up to but not including 1.0.

for i in range(5):
  x = random.randint(5,10)
  print(x)

t = [68,27,41,65,99,85,2,13,54,74,12,562,510]
random.choice(t)

"""# **Iteration**

### Maximum and minimum loops
"""

largest = None
print('Before', largest)
for itervar in [3,41,12,9,74,15]:
  if largest is None or itervar > largest:
    largest = itervar
  print('Loop:', itervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
  if smallest is None or itervar < smallest:
    smallest = itervar
  print('Loop:', itervar, smallest)
print('Smallest:', smallest)

"""**Q1** : Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
"""

rlist = []
while True:
  try:
    entry = input("Enter a number:")
    if type(int(entry)) == int:
      rlist.append(int(entry))
  except ValueError:
    if entry =="done":
      break
    print("Invalid input") 
print("Count: ", len(rlist))
print("Total: ",sum(rlist))
print("Average: ",sum(rlist) / len(rlist))

"""**Q2:** Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""

rlist = []
while True:
  try:
    entry = input("Enter a number:")
    if type(int(entry)) == int:
      rlist.append(int(entry))
  except ValueError:
    if entry =="done":
      break
    print("Invalid input") 

largest = None
for itervar in rlist:
  if largest is None or itervar > largest:
    largest = itervar
print('Largest:', largest)

smallest = None
for itervar in [3, 41, 12, 9, 74, 15]:
  if smallest is None or itervar < smallest:
    smallest = itervar
print('Smallest:', smallest)
