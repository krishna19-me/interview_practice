list1 = [10, 5, 3, 4, 3, 5, 6]

def find_repeating(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return f"Element is {lst[i]} and pos is {i}"
    return -1

print(find_repeating(list1))