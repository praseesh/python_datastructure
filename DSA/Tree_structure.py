class Node:
    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None

class BinarySearchTree:
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
                    
    def pre_order_traversal(self, root):
        if root is None:
            return 
        print(root.data,end="-> ")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)
        
                    
    def contains(self,data):
        current_node = self.root
        while current_node is not None:
            if data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return True
            
        return False
    
    def get_minimum(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node 
    
    
bst = BinarySearchTree()

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(6)
bst.insert(7)

# print(bst.contains(40))
# print(bst.contains(25))

bst.pre_order_traversal(bst.root)