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
        
    def in_order_helper(self, node):
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data, end=" ->  ")
            self.in_order_helper(node.right)
    def in_order(self):
        self.in_order_helper(self.root)
        
                    
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
    def remove(self,node, data):
        if not node:
            return None
        if data < node.data:
            node.left = self.remove(node.left,data)
        elif data > node.data:
            node.right = self.remove(node.right,data)
        else:
            if not node.left and node.right is None:
                node = None
                return node
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.get_minimum(node.right)
            node.data = temp.data
            node.right = self.remove(node.right,temp.data)
            
        return node
                
        
        
    
bst = BinarySearchTree()

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(6)
bst.insert(7)

bst.remove(bst.root,6)
# print(bst.contains(6))
# print(bst.contains(25))

bst.in_order()

# bst.pre_order_traversal(bst.root)