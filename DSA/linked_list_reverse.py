class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def print_linked_list(self, node):
        while node:
            print(node.val, end=" -> " if node.next else "")
            node = node.next
        print()
    
sol = Solution()
head = [1,2,3,4,5,6,7]
for i in head:
    sol.append(i)
    
print("Original List:")
sol.print_linked_list(sol.head)

reversed_head = sol.reverseList(sol.head)
print("Reversed List:")
sol.print_linked_list(reversed_head)

# reversed_head = sol.reverseList(sol.head)
# print("Reversed List:")
# sol.print_linked_list(reversed_head)