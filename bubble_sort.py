#nums=[5,8,1,6,9,2,4]
nums=[1,2,3,5,7,9]
def bubble(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range (0,i+1):
            if nums[j]> nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        if is_swap==False:
            return nums
bubble(nums)
print(nums)
