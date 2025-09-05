nums1 = [3,2,1]
nums2 = [1,2]
nums3=[2,2,3,1]

def brute(nums):
    n=len(nums)
    nums=list(set(nums))
    if n<3:
        return max(nums)
    elif n>=3:
        nums.sort(reverse=True)
        return nums[2]
print(brute(nums3))    
      
