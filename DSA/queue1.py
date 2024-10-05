class Node:
    def __init__(self,data):
        self.data = data
        self.node= None
        
class QueueTest:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None: