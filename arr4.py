nums1=[1,1,1,2,3,4,4,7,9,9,9,10]
nums2=[6,7,8,10]
#Unique elements in a sorted array
def duplicates(nums):
    n= len(nums)
    i=0
    j=i+1
    while j <n :
         if nums[i]!=nums[j]:
              i+=1
              nums[i],nums[j]=nums[j],nums[i]
         j+=1
    print(f"Size of new list is :{i+1}")
    return nums
print(f"new list is :{duplicates(nums1)}")
print(f"new list is :{duplicates(nums2)}")