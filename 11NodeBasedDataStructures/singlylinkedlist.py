class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Head = None

def insert(value):
    global Head
    new_node = Node(value)
    if Head is None:
        Head = new_node
    else:
        temp = Head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

def display():
    temp = Head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")

insert(100)
insert(200)
insert(300)

print("Linked List: ", end="")
display()
