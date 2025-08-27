#Using dictionary,universal for any constraint of n
n=[12,1,6,9,12,12,3,7,9,6,5,201]
m=[12,8,6,72,9,5]
freq={}
for num in n:
   freq[num]=freq.get(num,0)+1
res={}
for num in m:
   if num in freq:
     res[num]=freq[num]
print(res)

#if constraint: 1<=n[i]<=10,then number hashing is possible using list.But only for small length of list.
# in that case:
n=[5,3,2,2,1,5,5,7,5,10]
hash_list=[0]*11
for num in n:
  hash_list[num]+=1
for num in m:
  if 1<=num<=len(hash_list):
    print(hash_list[num],num)
  else:
   print(0,num)

