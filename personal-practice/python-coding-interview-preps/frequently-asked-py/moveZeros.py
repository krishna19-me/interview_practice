def moveZero(nums):
    l,r=0,0
    while r<len(nums):
        if nums[r]!=0:
            # print(nums[l],l,"....",nums[r],r)
            nums[r],nums[l]=nums[l],nums[r]
            l+=1
        r+=1
    return nums   
print(moveZero([1,2,0,4,0,15]))  