#How to create a node and store vale in SLL - less efficient
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

#linking all the nodes
node1.next=node2
node2.next=node3
node3.next=node4
print(node1.value)

print(node1.next)#stores the address of the next node
print(node2)#displays where the object is present
print(node2.value)
print(node1.next.next.next)#Node4
print(node4)
print(node1.next.next.next.next)