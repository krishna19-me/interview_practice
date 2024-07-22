array = [1, 2, 2, 3, 3, 4]
from collections import Counter

def freq(array, k):
    arrayset = set(array)
    dict1 = {}
    result = []
    for i in arrayset:
        dict1[i] = array.count(i)
        if dict1[i] >= k:
            result.append(i)
    return result


def method2(array, k):
    dict1 = {}
    for i in array:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return [num for num, count in dict1.items() if count >= k]

def method3(array, k):
    counters = Counter(array)
    return [count for count in counters if counters[count]>=k]

print(freq(array, 2))
print(method2(array, 2))
print(method3(array, 2))
