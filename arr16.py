nums=[3,1,6,8,-2,-5,-7,-3,2,-4]
#O(N+N/2)
def brute(arr):
    pos=[x for x in arr if x>0]
    neg=[x for x in arr if x<0]
    for i in range(0,len(pos)):
        arr[2*i]=pos[i]
        arr[(2*i)+1]=neg[i]
    return arr
print(brute(nums))

#Optimal
def optimal(arr):
    posindex=0
    negIndex=1
    result=[0]*len(arr)
    for num in arr:
      if num>0:
        result[posindex]=num
        posindex+=2
      else:
        result[negIndex]=num
        negIndex+=2
    return result
print(optimal(nums))