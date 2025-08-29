#Brute Force O(n^2)
nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
max_sum=float("-inf")
for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum=sum+nums[j]
        max_sum=max(sum,max_sum)
print(max_sum)

#Kadanes Algorithm-->O(n)
max_sum=float("-inf")
total=0
for num in nums:
    total=total+ num
    max_sum=max(max_sum,total)
    if total<0:
        total=0
print(max_sum)