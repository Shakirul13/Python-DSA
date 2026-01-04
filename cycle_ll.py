#cycle detection in linked list
#Brute force-Just logic
temp=head
my_set=set()
while temp is not None:
    if temp in my_set:
        print(True)
    my_set.add(temp)
    temp=temp.next
print(False)

#Optimal 
#Floyd Cycle detection
slow=head
fast=head
temp=head
while temp is not None and temp.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        print(True)
print(False)