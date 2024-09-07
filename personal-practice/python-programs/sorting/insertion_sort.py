nums = [3, 6, 5, 1, 2]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i -1
        while j >=0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = temp
    return nums
insertion_sort(nums)
print(nums)
