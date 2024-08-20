#Longest decreasing subsequence in a list

# arr = [10, 9, 2, 5, 3, 7, 101, 18]

# def LDS(arr):
    
#     curr_sequence = [1] * len(arr)
#     for i in range(1, len(arr)):
#         for j in range(i):
#             if arr[j] > arr[i]:
#                 curr_sequence[i] = max(curr_sequence[i], curr_sequence[j]+1)
                
#     return max(curr_sequence)

# print(LDS(arr))

def longest_decreasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return []

    # Initialize a list to store the length of the longest decreasing subsequence ending at each index
    lds = [1] * n

    # Fill lds array
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    # Find the maximum length from lds array
    max_length = max(lds)

    # Reconstruct the longest decreasing subsequence
    lds_sequence = []
    for i in range(n-1, -1, -1):
        if lds[i] == max_length:
            lds_sequence.append(arr[i])
            max_length -= 1

    return lds_sequence[::-1]  # Reverse the sequence to get the correct order


# Example usage:
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("Longest Decreasing Subsequence:", longest_decreasing_subsequence(arr))


# def LIS(arr):
    
#     curr_sequence = [1] * len(arr)
#     for i in range(1, len(arr)):
#         for j in range(i):
#             if arr[j] < arr[i]:
#                 curr_sequence[i] = max(curr_sequence[i], curr_sequence[j]+1)
                
#     return max(curr_sequence)

# arr = [10, 9, 2, 5, 3, 7, 101, 18]
# print(LIS(arr))