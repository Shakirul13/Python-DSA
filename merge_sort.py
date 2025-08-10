def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_array(left,right)

def merge_array(n,m):
  result=[]
  i,j=0,0
  p,q=len(n),len(m)
  while i<p and j<q:
    if n[i]<= m[j]:
      result.append(n[i])
      i+=1
    else:
      result.append(m[j])
      j+=1
  if i<p:
    while i<p:
      result.append(n[i])
      i+=1
  if j<q:
    while j<q:
      result.append(m[j])
      j+=1
  return result
 
nums=[9,3,6,9,10,12,1,4,2]
res=merge_sort(nums)
print(res)


