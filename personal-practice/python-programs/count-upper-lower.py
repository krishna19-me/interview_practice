string = "Hello! This is Krishna Murthy"


def count_lower_upper(string):
    lowercount = 0
    uppercount = 0
    for ch in string:
        if ch.islower():
            lowercount += 1
        elif ch.isupper():
            uppercount += 1

    return lowercount, uppercount


print(count_lower_upper(string))
