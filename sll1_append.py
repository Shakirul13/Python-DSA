class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Singlelinkedlist:
    def __init__(self):
        self.head=None
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def traversal(self):
        if self.head==None:
            print("SLL is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
sll=Singlelinkedlist()
#sll.traversal()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traversal()