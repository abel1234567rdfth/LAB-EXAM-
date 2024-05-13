class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1
    def push(self, item):
        if self.top == self.capacity - 1:
            print("Stack Overflow: Cannot push item, stack is full.")
            return
        self.top += 1
        self.stack[self.top] = item
    def pop(self):
        if self.top == -1:
            print("Stack Underflow: Cannot pop item, stack is empty.")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item
    def peek(self):
        if self.top == -1:
            print("Stack is empty.")
            return None
        return self.stack[self.top]
    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)

print(f"Top : {stack.peek()}")
print(f"Popped : {stack.pop()}")
while not stack.is_empty():
    print(f"Remaining elements: {stack.pop()}")
    break
