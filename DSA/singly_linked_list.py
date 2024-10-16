class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def delete(self, data):
        temp = self.head
        previous = None
        
        if temp is not None and temp.data == data:
            self.head =temp.next
            return
        while temp is not None and temp.data != data:
            previous = temp
            temp = temp.next
            
        if temp is None:
            print("Data is not found in the list")
            return
        
        previous.next = temp.next
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            
    
    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        previous = None
        count = 0
        
        while current is not None and count < position:
            previous = current
            current = current.next
            count += 1
            
        print("Count:  ",count)  
        if previous is None:
            print("Data is not found in the list")
            
        new_node.next = previous.next
        previous.next = new_node
        
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return
            
linked_list = LinkedList()

linked_list.append("This is my new LInked List")
linked_list.append("1")
linked_list.append("2")
linked_list.append("3")
linked_list.append("4")
linked_list.append("5")
linked_list.append("6")
linked_list.append("Last Linked list")

# linked_list.print()

# linked_list.delete("4")

# linked_list.print()

linked_list.insert(10,11)
linked_list.print()
