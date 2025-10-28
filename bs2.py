nums=[1,3,4,5,8,9,14,15,19,20,21]
target1=17
target2=30
#Brute force 
def linear(nums,target):
    n=len(nums)
    for i in range (0,n):
        if nums[i]>=target:
            return i
    return n
print(linear(nums,target1))

#Optimal 
def binary(nums,target):
    n=len(nums)
    lb=n
    low=0
    high=n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
print(binary(nums,target2))