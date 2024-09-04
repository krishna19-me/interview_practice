list1 = [10, 5, 3, 4, 3, 5, 6]

def find_repeating(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return f"Element is {lst[i]} and pos is {i}"
    return -1

print(find_repeating(list1))

def find_repeating_1(lst):
    set = dict()
    idx = -1
    for i in range(len(lst)):
        if lst[i] in set:
            idx = i
        else:
            set[lst[i]] =1
    return f"Element is {lst[idx]}"

print(find_repeating_1(list1))