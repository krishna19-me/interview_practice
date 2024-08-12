lst = [[1, 2], [3, 4], [2, 3], [5, 1], [7, 1, 2]]


def flatten_and_count(lst):
    flatlst = []
    dict1 = {}
    for l in lst:
        flatlst.extend(l)
    for num in flatlst:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    return dict1


print(flatten_and_count(lst))
