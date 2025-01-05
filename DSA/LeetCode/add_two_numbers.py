class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1, head2 = l1, l2
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        A, n = ListNode(0), 0
        new_head = A
        while (head1 != None) or (head2 != None):
            if head1 is None:
                m = head2.val + int(n)
                n = 0
                head2 = head2.next
            elif head2 is None:
                m = head1.val + int(n)
                n = 0
                head1 = head1.next
            else:
                m = head1.val + head2.val + int(n)
                n = 0
                head1 = head1.next
                head2 = head2.next
            m = str(m)
            if len(m) > 1:
                n = m[0]
                new_head.next = ListNode(m[1])
            else:
                new_head.next = ListNode(m)
            if ((head1 and head2) == None) and len(m) > 1:
                new_head.next.next = ListNode(n)
            new_head = new_head.next
        return A.next
sol = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
s = sol.addTwoNumbers(l1,l2)
print(s)