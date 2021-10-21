from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self, value):
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        
    def dequeue(self):
        pass

    def peek(self):
        pass
    
    def is_empty(self):
        return not self.front