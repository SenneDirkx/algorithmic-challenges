# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = ListNode(0)
        root = current
        while l1 is not None or l2 is not None:
            if l1 is None:
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val >= l2.val:
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif l2.val > l1.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            current = current.next
        return root.next

# Runtime: 28 ms (faster than 98.51% of online Python3 submissions)
# Memory Usage: 12.8 MB (less than 100.0% of Python3 online submissions)