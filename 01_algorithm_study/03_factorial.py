# -*- coding: utf-8 -*-
"""**Q3:** The algorithm of the program that takes the factorial of an entered number ."""

number = int(input("Enter a number: "))
fac = 1

if number < 0:
  print("The factorial of negative numbers cannot be calculated.")
elif number == 0:
  print("0!=1")
else:
  for i in range(1, number+1):
    fac = fac * i
  print(number," factorial of the number", fac)
