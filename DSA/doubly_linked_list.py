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
        
    def modify(self,data, position):
        current = self.head
        count = 0
        
        while current is not None:
            if count == position:
                current.data = data
                return 
            current = current.next
            count+=1   
        print("Position is out of bounds.")
    
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            if self.tail is None:  
                self.tail = new_node
            return
        current = self.head
        # prev = None
        count = 0
        
        while current is not None and count < position -1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of bounds")
            return
        
        # If inserting at the tail
        if current.next is None:
            self.append(data)
            return
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
            

        
    def print(self):
        temp = self.head
        while temp:
            prev_data = temp.prev.data if temp.prev else None
            next_data = temp.next.data if temp.next else None
            print(f"Data: {temp.data}, Previous: {prev_data}, Next: {next_data}", end=" → \n")
            temp = temp.next
            
    def print_reverse(self):
        temp = self.tail
        while temp is not None:
            print(f"Data: {temp.data}", end=" → \n")
            temp = temp.prev        
            
linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.append("3")
linked_list.append("4")
linked_list.append("5")
linked_list.append("6")

linked_list.modify(10,3)
linked_list.print()
# linked_list.print_reverse()

linked_list.insert(22,4)

# linked_list.print()
linked_list.print_reverse()
