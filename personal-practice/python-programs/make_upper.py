string = "hello world"
lst = string.split(" ")


def make_upper(s):
    return s[0].upper()+s[1:len(s)-2]+s[len(s)-1].upper()


for l in lst:
    print(make_upper(l))
