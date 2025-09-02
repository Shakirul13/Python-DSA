#majority element in an array
nums=[1,3,1,2,1,1,2]

#brute force
def brute(arr):
   freq_map={}
   for num in arr:
     freq_map[num]=freq_map.get(num,0)+1
   return max(freq_map,key=freq_map.get)
print(brute(nums))

#Optimal space complexity
def optimal(arr):
    count=0
    candidate=None
    for num in arr:
        if count==0:
           candidate=num
        if num==candidate:
           count+=1
        else:
           count-=1
    return candidate
print(optimal(nums))
      