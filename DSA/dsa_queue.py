class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is  None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        if self.front is None:
            print("The Queue is Empty!.. ")
            return
        self.front = self.front.next
        if self.front is None:
            self.rear = None
    def display(self):
        current = self.front
        if current is None:
            print("Queue is Empty!")
            return
        while current is not None:
            print(f"{current.data} -> ", end="")  
            current = current.next
        print("None")
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()
