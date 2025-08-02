n=int(input("Enter a number:"))
new =n
sum=0
r=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**r
    n=n//10
if sum==new:
    print("Armstrong")
else:
    print("Not Armstrong")