class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
dll.append(5)
dll.append(15)
dll.append(25)

print("Doubly Linked List:")
dll.display()

print("After deleting 15:")
dll.delete_node(15)
dll.display()
