n1=121
n2=140
def palindrome(n):
   new=n
   rev=0
   while n>0:
    digit=n%10
    n=n//10
    rev=rev*10 + digit
   if rev==new:
    return True
   else:
    return False
print(palindrome(n1))
print(palindrome(n2))