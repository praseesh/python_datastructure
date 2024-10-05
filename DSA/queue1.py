class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        
class QueueTest:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            print("Queue Created Successfully")
            return
        if self.front and self.rear:
            self.rear = new_node
            self.rear.next = new_node
            print("Queue Added Successfully")
            
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        self.front = self.front.next
        print(f"{self.front.data} Removed Successfully")
    def display(self):
        pass

queue = QueueTest()            
            
        