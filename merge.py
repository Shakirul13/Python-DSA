n= [ 1,2,2,2,4,6,6,7,9]
m=[1,4,6,8]
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
k=merge_array(n,m)  
print(k)   
      


