class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Singlelinkedlist:
    def  __init__(self):
        self.head=None
    def insert_at(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
             current=self.head
             previous_node=None 
             count=0
             while current is not None and count<position:
                 previous_node=current
                 current=current.next
                 count+=1
             previous_node.next=new_node
             new_node.next=current
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")  
ll=Singlelinkedlist()
ll.insert_at(10,0)
ll.insert_at(20,1)
ll.insert_at(30,2)
ll.insert_at(40,2)
ll.insert_at(50,1)
ll.display()
