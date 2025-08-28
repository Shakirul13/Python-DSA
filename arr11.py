nums=[5,9,1,2,4,15,6,3]
target=13
#takes O(n^2) time
n=len(nums)
for i in range(0,n-1):
    for j in range (i+1,n):
        if nums[i]+nums[j]==target:
            print([i,j])
#takes O(n) time
hash_map={}
n=len(nums)
for i in range(0,n):
    left=target-nums[i]
    if left in hash_map:
        print([hash_map[left],i])
    hash_map[nums[i]]=i