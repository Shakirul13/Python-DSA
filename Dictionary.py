n=[1,4,7,9,4,7,7,2,6]

hash_map=dict()
for i in n:
     if i in hash_map:
         hash_map[i]+=1

     else:
         hash_map[i]=1
print(hash_map)

#Using get() function:
freq={}
for i in n:
    freq[i]=freq.get(i,0)+1
print(freq)