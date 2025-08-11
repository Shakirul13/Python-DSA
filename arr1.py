nums=[55,32,-97,99,3,67]
res=nums[0]
n=len(nums)-1
for num in nums[1:]:
    if num>res:
        res=num
    
print(res)