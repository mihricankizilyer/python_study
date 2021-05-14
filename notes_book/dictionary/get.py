word = 'brontosaurus'
d = dict()
for c in word:
  if c not in d:
    d[c] = 1
  else:
    d[c] = d[c] + 1
print(d)



# get method automatically handles the case where a key is not in a dictionary
word = 'brontosaurus'
d = dict()
for c in word:
  d[c] = d.get(c,0) + 1
print(d)

