nums = [12, 3, 4, 5, 233, 56]


def selection_sort(nums):
    for i in range(len(nums)-1):
        curr_min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[curr_min_idx]:
                curr_min_idx = j
        nums[i], nums[curr_min_idx] = nums[curr_min_idx], nums[i]


selection_sort(nums)
print(nums)
