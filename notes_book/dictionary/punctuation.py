# -*- coding: utf-8 -*-
"""punctuation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1780tUVgE83luKfKDASBm3tkpOEBQFLcu
"""

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# deletestr parameter to delete all of the punctuation.

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
