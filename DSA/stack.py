class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    def display(self):
        current = self.top
        while current is not None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")
        
stack = Stack()
stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")
stack.push("5")
stack.display()