s='aCAjaCCdj'
q=["a","C","j"]
hash_list=[0]*57
for ch in s :
    ascii_val=ord(ch)
    index=ascii_val-65
    hash_list[index]+=1
for ch in q :
    ascii_val=ord(ch)
    index=ascii_val-65
    print(hash_list[index],ch)