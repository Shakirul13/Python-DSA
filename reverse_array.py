nums=[5,9,8,3,6,7,1,4,2]
def reverse(nums,L,R):
    if L>=R:
        return
    nums[L],nums[R]=nums[R],nums[L]
    reverse(nums,L+1,R-1)
L=int(input("Enter the index from where you want to reverse:"))
R=int(input("Enter the index upto which you want to reverse:"))
reverse(nums,L,R)
print(nums)