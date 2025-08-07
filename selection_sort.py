nums=[5,7,8,4,1,6,9,2]
n=len(nums)
def selection(nums):
    for i in range(0,n):
        max_index=i
        for j in range (i+1,n):
            if nums[j]>nums[max_index]: #incase of ascending order when nums[j]<nums[max_index]
                max_index=j
        nums[i],nums[max_index]=nums[max_index],nums[i]
selection(nums)
print(nums)