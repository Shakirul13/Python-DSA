nums=[2,8,5,7,10]
largest=nums[0]
for i in range(1,len(nums)):
    if largest<nums[i]:
        second_largest=largest
        largest=nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
print(second_largest)