nums=[5,12,3,9,8,1,7]
n=len(nums)
k=int(input("Enter the no of places to be rotated:"))
k=k%n
#Using slicing
# nums[:]=nums[n-k:]+ nums[:n-k]
# print(nums)
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)
print(nums)