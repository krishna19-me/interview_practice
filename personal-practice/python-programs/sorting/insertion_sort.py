nums = [3, 6, 5, 1, 2]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            print(nums[j-1])
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1


insertion_sort(nums)
print(nums)
