string = "Madam"


def check_palindrome(string):
    newstr = ''.join([i.lower() for i in string])
    # return string == string[::-1]
    return newstr == newstr[::-1]


def normal(string):
    newstr = ""
    for i in range(len(string)-1, -1, -1):
        newstr += string[i]
    print(string)
    print(newstr)
    return newstr.lower() == string.lower()


print(normal(string))
print(check_palindrome(string))


# SWAP

def swap(a, b):
    a, b = (a+b-a), (a+b-b)
    print(a, b)
    # a, b = b, a
    return a, b


print(swap(10, 20))
