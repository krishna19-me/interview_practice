import re 


word1="0ab2123" 
word="ab2123" 

print(bool(re.match('^[0-9]',word1))) #starting as 0

print(bool(re.match('[A-Za-z0-9]+$',word))) #alphanum



