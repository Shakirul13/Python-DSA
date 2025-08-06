#Using Recursion 
def palindrome(s,left,right):
  if left>=right:
    return True
  if s[left]!= s[right]:
    return False
  return palindrome(s,left+1,right-1)

def main():
  s="orange"
  if palindrome(s,0,len(s)-1):
    print("palindrome")
  else:
    print("Not palindrome")
main()

#Using loop
# s="orange"
# l=0
# r=len(s)-1
# while l<r:
#   if s[l]!=s[r]:
#     print("Not palindrome")
#   l+=1
#   r-=1
# print("Palindrome")