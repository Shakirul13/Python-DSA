nums=[1,1,0,1,1,0,0,1,1,1,1]
def ones(nums):
  max_count=0
  count=0
  for i in range(0,len(nums)):
    if nums[i]==1:
        count+=1
    else:
        max_count=max(max_count,count)
        count=0
  return max(max_count,count)

print(ones(nums))  