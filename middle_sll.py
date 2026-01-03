#For odd and even length linked list
#Brute Force
class Middle:
    def mid(self):
      n=0
      temp=self.head
      while temp is not None:
         n+=1
         temp=temp.next
      temp=self.head
      for _ in range(0,n//2):
         temp=temp.next
      return temp
  

#Optimal
#Tortoise-Hare Approach
fast=head
slow=head
while fast is not None and fast.next is not None:
   slow=slow.next
   fast=fast.next.next
print(slow)