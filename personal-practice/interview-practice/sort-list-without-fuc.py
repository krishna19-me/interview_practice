list1 = [12, 3, 45, 6, 7]


def sort_wihout_func(list1):
    result = []
    while list1:
        minimum = list1[0]
        for i in list1:
            if i < minimum:
                minimum = i
        result.append(minimum)
        list1.remove(minimum)
    return result


print(sort_wihout_func(list1))
