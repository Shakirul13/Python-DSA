nums=[2,-7,62,5,90,0,8]
#Using slicing
n=len(nums)
# nums[:]= [nums[-1]]+ nums[0:n-1]
# print(nums)
temp=nums[-1]
for i in range (n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)
