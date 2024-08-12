

import re
def lonestword(s):
  words=s.split()
  d={}
  for word in words:
    if bool(re.match('[a-zA-Z]+$',word)):
      d[word]=len(word)
#   print(d)

  if d:
    return [max(d)]
  else:
     return -1     

s="kart2hi loki marimass22"
print(lonestword(s))