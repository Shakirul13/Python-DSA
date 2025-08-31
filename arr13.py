#Print the number with the occurance of 1.
nums=[4,2,3,2,1,1]
hash_map={}
for i in range (0,len(nums)):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
for num in hash_map:
    if hash_map[num]==1:
        print(num)
        