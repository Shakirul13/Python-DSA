nums=[1,1,1,2,3,4,4,7,9,9,9,10]
n= len(nums)
i=0
j=i+1
while j <n :
    if nums[i]!=nums[j]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(nums)
print(f"Size of new list is :{i+1}")