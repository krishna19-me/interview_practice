lst = [10, 21, 22, 100, 101, 200, 300]

def countPossibleTriangles(lst):
    lst.sort()
    print("list", lst)
    count =0
    for i in range(len(lst) - 1, 0 , -1):
        start = 0
        print("start", lst[start])
        end = i-1
        print("end", lst[end])
        print("ith element", lst[i])
        while start< end:
            if lst[start] + lst[end] > lst[i]:
                #here if lst[start] + lst[end] > lst[i] then all elements between start to end satisfies the condtion because lst is sorted
                count+= (end-start)
                end-=1
            else:
                start+=1

    return count

print(countPossibleTriangles(lst))

