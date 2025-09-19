nums=[2,5,8,12,19,46,131]
target=46
#Iterative Approach
def binarysearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(binarysearch(nums,target))

#Recursive Approach
def bs(nums,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if nums[mid]<target:
        return bs(nums,mid+1,high,target)
    elif nums[mid]==target:
        return mid
    else:
        return bs(nums,low,mid-1,target)
print(bs(nums,0,len(nums)-1,target))