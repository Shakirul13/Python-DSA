arr=[-1,0,1,2,-1,-4]
#Brute force solution: O(n^3)
def brute(arr):
    n=len(arr)
    res=set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    temp=[arr[i],arr[j],arr[k]]
                    temp.sort()
                    res.add(tuple(temp))
    return [list(ans)for ans in res]
print(brute(arr))

#Better solution by eliminating the 3rd pointer
#arr[k]=-(arr[i]+arr[j])
def better(arr):
    res=set()
    for i in range(0,len(arr)):
        my_set=set()
        for j in range(i+1,len(arr)):
            k=-(arr[i]+arr[j])
            if k in my_set:
                temp=[arr[i],arr[j],k]
                temp.sort()
                res.add(tuple(temp))
            my_set.add(arr[j])
    return [list(ans)for ans in res]
print(better(arr))

def Optimal(nums):
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(0,n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res
print(Optimal(arr))