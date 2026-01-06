#return the starting point from where the cycle starts
#brute force
#logic
temp=head
my_set=set()
while temp is not None:
    if temp in my_set:
        print(temp)
    my_set.add(temp)
    temp=temp.next
print("No cycle present")

#Optimal solution
fast=head
slow=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
