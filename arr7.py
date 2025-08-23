nums=[1,0,2,4,3,0,0,3,5,1]
#Brute Force
temp=[]
for num in nums:
    if num!=0:
        temp.append(num)
n=len(temp)
for i in range (0,n):
    nums[i]=temp[i]
nums[n:]=[0]*(len(nums)-n)
print(nums)

#Optimal Solution
def zeroes(nums):
 if len(nums)==1:
    return
 i=0
 while i<len(nums):
    if nums[i]==0:
       break
    i+=1
 if i==len(nums):
    return
 j=i+1
 while j<len(nums):
    if nums[j]!=0:
       nums[i],nums[j]=nums[j],nums[i]
       i+=1
    j+=1
 return nums
print(zeroes(nums))