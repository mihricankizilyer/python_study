# -*- coding: utf-8 -*-
"""
# Chapter 7: **FILES**

"""

fhand = open('mbox.txt')
print(fhand)

fhand = open('/content/mbox.txt')
count = 0
for line in fhand:
  count = count +1 
print('Line Count:', count)

fhand = open('/content/mbox.txt')
inp = fhand.read()
print(len(inp))

"""Remember that this form of the open function should only be used if the file data
will fit comfortably in the main memory of your computer. If the file is too large
to fit in main memory, you should write your program to read the file in chunks
using a for or while loop.
"""

fhand = open('/content/mbox.txt')
count = 0
for line in fhand:
  if line.startswith('From'):
    print(line)

fhand = open('/content/mbox.txt')
for line in fhand:
  line = line.rstrip()
  if line.startswith('From'):
    print(line)

fhand = open('/content/mbox.txt')
for line in fhand:
  line = line.strip()
  if line.find('@uct.ac.za') == -1 : continue
  print(line)

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith('Subject'):
    count = count + 1
print('There were', count, 'subjecy lines in', fname)

fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('file cannot be opened', fname)
  exit()
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print('there where ', count,'subejcy lines in ', fname)

"""Exercise 1: Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:

"""

fname = open('/content/mbox.txt')
for line in fname:
  print(line.upper())

"""Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:

"""

fname = open('/content/mbox.txt')
for line in fname:
  if line.find('X-DSPAM-Confidence: 0.8475') == -1 : continue
  print(line)
