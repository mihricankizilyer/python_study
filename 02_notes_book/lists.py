# -*- coding: utf-8 -*-
"""
# Chapter 8: **LİSTS**
"""

numbers = [21,1,2,5,41,2,65,2,15,51]
rlist=[]
for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2
  rlist.append(numbers[i])

print(rlist)

numlist = []
while True:
  inp = input('Enter number: ')
  if inp == "done": break
  numlist.append(float(inp))
print(sum(numlist) / len(numlist))
