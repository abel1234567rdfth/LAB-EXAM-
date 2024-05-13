class QueueUsingTwoStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []
    def enqueue(self, item):
        self.inbox.append(item)
    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            return None
        return self.outbox.pop()
    def peek(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            return None
        return self.outbox[-1]
    def is_empty(self):
        return not (self.inbox or self.outbox)
queue = QueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Dequeued: {queue.dequeue()}")
print(f"Dequeued: {queue.dequeue()}")
print(f"Peek: {queue.peek()}")
