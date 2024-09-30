class Node:
    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        current_node = self.root
        if self.root == None:
            self.root = Node(data)
            return
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(data)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(data)
                    break
                else:
                    current_node = current_node.right