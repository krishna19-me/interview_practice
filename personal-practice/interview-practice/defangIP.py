import re

string = "1.1.1.1"
# newstr = ""
# for s in list(string):
#     if s == ".":
#         newstr+="[.]"
#     else:
#         newstr+=s

# print(newstr)

newstr = string.replace(".","[.]")
print(newstr)
# re.findall(string,)