nums = [4, 2, 4, 6, 7, 1]
nums = [19, 18, 37, 1, 2, 3, 45]


def sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


sort(nums)
print(nums)
