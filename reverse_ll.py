#Reverse a linked list:logic
#Brute force solution : reverse the ll by changing the value
#5->7->10->2->80->
temp=head
stack=[]
while temp is not None:
    stack.append(temp.val)
    temp=temp.next
temp=head
while temp is not None:
    e=stack.pop()
    temp.val=e
    temp=temp.next
#optimal
temp=head
prev=None
while temp is not None:
    front=temp.next
    temp.next=prev
    prev=temp
    temp=front
prev