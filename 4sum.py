nums=[1,0,-1,0,-2,2]

#Brute force approach O(n^4)
def brute(nums):
    target=0
    n=len(nums)
    res=[]
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                         temp=[nums[i],nums[j],nums[k],nums[l]]
                         temp.sort()
                         res.append(temp)
    return res
print(brute(nums))

#Optimal solution O(n^3)
nums2=[1,1,1,1,2,2,3,3,3,4,4,4,5,5]
def optimal(nums):
    target=8
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(0,n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1
            while k<l:
                total=nums[i]+nums[j]+nums[k]+nums[l]
                if total==target:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
                elif total < target:
                    k+=1
                else:
                    l-=1
    return ans
print(optimal(nums2))
