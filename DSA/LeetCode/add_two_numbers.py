class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize the dummy node and the carry variable
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 is not None or l2 is not None or carry:
            # Get the value of the current nodes or 0 if the node is None
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move the pointers forward
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy.next

# Helper function to convert a list to a ListNode linked list
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linkedlist(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))

# Create linked lists for l1 = [2, 4, 3] and l2 = [5, 6, 4]
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])

# Call the function
sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Print the result
print_linkedlist(result)
