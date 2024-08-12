import re
lst = ['Sam200', 'Mon1u100', 'Zaid130', 'Mukesh50', 'Nisha99']


def sort_alphanum(lst):
    dict1 = {}
    for l in lst:
        dict1[l] = int("".join(re.findall("[0-9]*", l)))
    print(dict1)
    resultdict = dict(sorted(dict1.items(), key=lambda x: x[1]))
    print(list(resultdict.keys()))


def sort_alphanum_normal(lst):
    dict1 = {}
    for l in lst:
        num = ""
        for i in l:
            if i.isdigit():
                num += i
        dict1[l] = int(num)
    print(list(dict(sorted(dict1.items(), key=lambda x: x[1])).keys()))


sort_alphanum(lst)
# sort_alphanum_normal(lst)
