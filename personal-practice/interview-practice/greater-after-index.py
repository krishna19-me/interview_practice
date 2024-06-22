input = [99, 28, 12, 55, 13, 15, 76, 99]
for i in range(len(input)):
    count = 0
    result = []
    for j in range(i+1, len(input)):
        if input[j] > input[i]:
            count += 1
            result.append(input[j])
    print(input[i], count, result)
