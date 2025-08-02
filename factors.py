n=int(input("Enter the number:"))
result=[]
#Brute Force--> N
# for i in range(1,n+1):
#     if n%i==0:
#         result.append(i)

#Better --> N/2
# for i in range (1,n//2):
#     if n%i==0:
#         result.append(i)
# result.append(n)

#Optimal Solution --> sqrt(N)+ NlogN (if sorting is done)
from math import sqrt
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        result.append(i)
        if n//i!=i:
          result.append(n//i)
result.sort()
print(result)
