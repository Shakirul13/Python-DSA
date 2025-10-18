nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target=int(input("Enter the target number from the given list:"))
#Upper Bound -- Smallest index such that nums[i]>target
def upper(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ub=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub

#Lower Bound -- Smallest index such that nums[i]>=target
def lower(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
print(f"The staring of the number is from:{lower(nums,target)}")
print(f"The ending of the number is upto:{upper(nums,target)}")