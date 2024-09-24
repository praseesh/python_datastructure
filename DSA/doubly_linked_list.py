class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev= self.tail
            self.tail = new_node
            
        tail = new_node
            
    def print(self):
        temp = self.head
        while temp is not None:
            print(f"Data: {temp.data}, Previous: {str(temp.prev) if temp.prev else None}, Next: {str(temp.next) if temp.next else None}", end=" → \n" if temp.next else "\n")
            temp = temp.next
            
linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.append("3")
linked_list.append("4")
linked_list.append("5")
linked_list.append("6")

linked_list.print()