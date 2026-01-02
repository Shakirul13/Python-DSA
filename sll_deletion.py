class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    def delete(self, val):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        if temp.val == val:
            self.head = temp.next
            return

        prev = temp
        temp = temp.next

        while temp:
            if temp.val == val:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Node not found")

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


# ✅ Create object AFTER class definition
ll = Singlelinkedlist()
ll.insert_at(10, 0)
ll.insert_at(20, 1)
ll.insert_at(30, 2)
ll.insert_at(40, 2)
ll.insert_at(50, 1)

ll.display()

ll.delete(50)
ll.delete(10)
ll.delete(99)

ll.display()
