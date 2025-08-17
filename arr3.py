def check(nums):
    n=len(nums)
    for i in range (0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums=[2,4,7,9,10]
res=print(check(nums))