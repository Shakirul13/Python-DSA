#Merge 2 sorted list with unique elemnts
nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
n=len(nums1)
m=len(nums2)
result=[]
i=0
j=0
while i<n and j<m:
    if nums1[i]<=nums2[j]:
        if len(result)==0 or nums1[i]!=result[-1]:
            result.append(nums1[i])
        i+=1
    else:
        if len(result)==0 or nums2[j]!=result[-1]:
            result.append(nums2[j])
        j+=1
while i < n:
    if len(result)==0 or nums1[i]!=result[-1]:
            result.append(nums1[i])
    i+=1
        
while j< m:
     if len(result)==0 or nums2[j]!=result[-1]:
            result.append(nums2[j])
     j+=1
print(result)