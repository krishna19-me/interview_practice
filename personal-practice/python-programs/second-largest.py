lst = [10, 20, 3, 40, 50]


def second_largest(lst):
    first, second = lst[0], lst[1]
    # print(first, second)
    if len(lst) < 2:
        return None
    if first < second:
        first, second = second, first

    for num in lst[2:]:
        if num > first:
            first, second = num, first
        elif num > second:
            second = num
    return second


def using_max_min(lst):
    largest = max(lst)
    return max([num for num in lst if num != largest])


print(second_largest(lst))
print(using_max_min(lst))
