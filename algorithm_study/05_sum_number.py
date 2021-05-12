# -*- coding: utf-8 -*-
"""sumnumber.ipynb

Program that adds 10 numbers entered on the keyboard

"""

rlist = []
for i in range(0,10):
  rlist.append(int(input()))
toplam = 0
for i in rlist:
  sum = sum + i
print(sum)
