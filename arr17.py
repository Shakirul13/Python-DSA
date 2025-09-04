#Longest consecutive sequence
nums1=[1,99,101,98,2,5,3,100,1,1]
nums2= [0,3,7,2,5,8,4,6,0,1]

#Brute Force
def brute(nums):
   n=len(nums)
   max_count=0
   for i in range(0,n):
      num=nums[i]
      count=1
      while num+1 in nums:
         count+=1
         num=num+1
      max_count=max(max_count,count)
   return max_count
print(brute(nums2))

#Better O(nlogn+n)~O(nlogn)
def better(nums):
 if not nums:
     return 0
 nums.sort()
 n=len(nums1)
 leng=1
 max_length=1
 for i in range (0,n-1):
    if nums[i+1]==nums[i]+1:
        leng+=1
    elif nums[i+1]!=nums[i]:
        max_length=max(leng,max_length)
        leng=1
 return max(max_length,leng)
print(better(nums1))

#Optimal Soulution O(n)
def optimal(nums):
    n=len(nums)
    new_set=set()
    for i in range(0,n):
      new_set.add(nums[i])
    longest=0
    for num in new_set:
       if num-1 not in new_set:
          x=num
          count=1
          while x+1 in new_set:
             count+=1
             x+=1
          longest=max(longest,count)
    return longest
print(optimal(nums2))