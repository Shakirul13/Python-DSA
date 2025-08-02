n=int(input("Enter the number:"))
new=n
rev=0
while n>0:
    digit=n%10
    n=n//10
    rev=rev*10 + digit
if rev==new:
    print("palindrome")
else:
    print("Not palindrome")
    