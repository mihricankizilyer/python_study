# -*- coding: utf-8 -*-
"""Strings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vRuICNcOX0tm0qo7AQ2xre4yphEJEcf8

# Chapter 6: **STRİNGS**

- Strings are immutable
"""

#greeting = 'Hello, world!'
#greeting[0] = 'J'
#TypeError: 'str' object does not support item assignment

#The best you can do is create a new string that is a variation on the original:
greeting = 'Hello World!'
new_greeting = 'J'+greeting[1:]
print(new_greeting)

index = 0
fruit = "banana"

while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1

count = 0
fruit = "banana"

for i in fruit:
  if i == "a":
    count = count + 1
print(count)

"""## Parsing strings"""

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

"""### Format operator

"""

#the format sequence %d means that the second operand should be formatted as an integer (“d” stands for “decimal”):
camels = 42
'I have spotted %d camels.' % camels

"""- %d to format an integer
- %g to format a floating-point number 
- %s to format a string
"""

#'%d %d %d' % (1, 2)
#TypeError: not enough arguments for format string

#'%d' % 'dollars'
#TypeError: %d format: a number is required, not str

str = 'X-DSPAM-Confidence:0.8475'
before = str.find(":")
k = str[before+1:]
print(float(k))