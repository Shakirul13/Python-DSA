#Buy and sell stocks
prices1=[7,2,1,5,6,4,8]
prices2=[7,6,5,4,3,2] #Edge case

#Brute Force --> O(n^2)
def brute(arr):
   n=len(arr)
   profit=0
   for i in range(0,n-1):
      for j in range(i+1,n):
        if arr[j]>arr[i]:
            diff=arr[j]-arr[i]
            profit= max(profit,diff)
   return profit
print(brute(prices1))

#Optimal
def optimal(arr):
  profit=0
  n=len(arr)
  min_price=float("inf")
  for i in range(0,n):
    min_price=min(min_price,arr[i])
    profit=max(profit,arr[i]-min_price)
  return profit
print(optimal(prices2))

