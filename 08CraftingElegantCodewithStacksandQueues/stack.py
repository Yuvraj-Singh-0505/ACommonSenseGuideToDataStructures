class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) >= 100:
            print("Stack overflow")
        else:
            self.stack.append(value)
            print(f"{value} pushed to the stack")

    def pop(self):
        if not self.stack:
            print("Stack underflow")
        else:
            popped = self.stack.pop()
            print(f"{popped} popped from the stack")

    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)

stack.display()
stack.peek()
stack.pop()
stack.display()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")
