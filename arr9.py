nums=[0,1,2,3,4,6,7]
n=len(nums)
for i in range(0,n+1):     #takes O(n^2) tc and O(1) sc
    if i not in nums:
        print(f"Number missing:{i}")
    
#Better using Dictionary
freq={}
for i in range(0,n+1):
    freq[i]=0
for num in nums:      #takes O(n) time complexity and space complexity
    freq[num]=1
for k,v in freq.items():
    if v==0:
        print(k)

#Optimal solution takes O(n) and O(1)     
def sum(nums):
  sums=0
  for i in range(0,len(nums)):
      sums+=nums[i]
  return sums
res=sum(nums)
expected=n*(n+1)//2
print(expected-res)